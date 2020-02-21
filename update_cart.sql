create or replace function update_cart()
returns trigger as
$body$
begin
  if ((new.user_name, new.cart_num) not in (select user_name, cart_num from cart1)) then
    insert into cart1 values (new.user_name, new.cart_num, new.restaurant_name, 0, 'NO', null);
  end if;
  insert into cart2 values (new.user_name, new.cart_num, new.food_name, new.food_num);

  update cart1
    set total_price = (select total_price from cart1 where cart1.cart_num = new.cart_num and cart1.user_name = new.user_name) +
                      (select menu.price * (100 - menu.discount) * new.food_num / 100 from menu where menu.restaurant_name = new.restaurant_name and menu.food_name = new.food_name)
      where new.cart_num = cart1.cart_num and cart1.user_name = new.user_name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;
create trigger update_cart_trigger
instead of insert on v_carts
for each row
execute procedure update_cart();

