create or replace function cal_res_score()
returns trigger as
$body$
begin
  update restaurant
    set score = (select avg(res_score) from pay
      where new.restaurant_name = pay.restaurant_name
      )
      where new.restaurant_name = restaurant.name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;
create trigger update_res_score_trigger
instead of update on v_payments
for each row
execute procedure cal_res_score();

