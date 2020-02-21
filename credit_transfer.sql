create or replace function credit_transfer()
returns trigger as
$body$
begin
  create table total_res_price(
    total_cost integer,
    primary key (total_cost)
  );
  insert into total_res_price (total_cost)
  select sum(menu.price * (100 - menu.discount) * cart2.food_num / 100) as total_cost
    from cart1,
    cart2,
    menu
    where cart1.cart_num = cart2.cart_num
    and cart1.user_name = cart2.user_name
    and menu.restaurant_name = cart1.restaurant_name
    and cart2.food_name = menu.food_name
    and cart1.user_name = new.user_name
    and cart1.cart_num = new.cart_num
    and cart1.user_name = new.user_name;


    if(new.payment_type = 'CASH' or (select credit from user1 where user1.user_name = new.user_name) >= (select * from total_res_price) + NEW.delivery_cost) then
    -- deliver_man
    if (new.payment_type = 'CREDIT') then
      update user1 as u1
    set credit = NEW.delivery_cost + (select credit from user1 as u2 where u2.user_name = u1.user_name)
      where u1.user_name = NEW.delivery_user_name;
--   costumer
  update user1 as u1
    set credit = - NEW.delivery_cost - (select * from total_res_price)
                     + (select credit from user1 as u2 where u2.user_name = u1.user_name)
      where u1.user_name = NEW.user_name;
--   restaurant
  update restaurant as r1
    set credit = (select * from total_res_price) + (select credit from restaurant as r2 where r2.name = r1.name)
      where r1.name = NEW.restaurant_name;
    end if;
  insert into pay values (new.user_name, new.cart_num, new.delivery_user_name, new.restaurant_name, new.payment_type, new.delivery_cost, new.res_score, new.dm_score);
    update deliver_man
    set score = (select avg(dm_score) from pay
      where new.delivery_user_name = pay.delivery_user_name
      )
      where new.delivery_user_name = deliver_man.user_name;
    update restaurant
    set score = (select avg(res_score) from pay
      where new.restaurant_name = pay.restaurant_name
      )
      where new.restaurant_name = restaurant.name;
  end if;

  drop table total_res_price;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;

create trigger credit_payment_trigger
instead of insert on v_payments
for each row
execute procedure credit_transfer();