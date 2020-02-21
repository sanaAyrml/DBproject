create or replace function inc_credit()
returns trigger as
$body$
begin
  insert into increase_user_credit values (new.user_name, new.amount, new.year, new.month, new.day, new.hour);
  update user1
    set credit = (select credit from user1 as u2
      where new.user_name = u2.user_name
      ) + new.amount
      where new.user_name = user1.user_name;

  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;
create trigger inc_credit_trigger
instead of insert on v_increase_credit
for each row
execute procedure inc_credit();

