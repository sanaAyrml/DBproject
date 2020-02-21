
create or replace function change_address_func()
returns trigger as
$body$
begin
    update costumer
        set chosen_address = 'No'
        where new.user_name = costumer.user_name and new.address <> costumer.address and new.chosen_address = 'YES';
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;

create trigger change_address_trigger
after insert or update on costumer
for each row
execute procedure change_address_func();