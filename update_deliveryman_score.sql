create or replace function cal_dm_score()
returns trigger as
$body$
begin
  update deliver_man
    set score = (select avg(dm_score) from pay
      where new.delivery_user_name = pay.delivery_user_name
      )
      where new.delivery_user_name = deliver_man.user_name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;
create trigger update_dm_score_trigger
instead of update on v_payments
for each row
execute procedure cal_dm_score();

