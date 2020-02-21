create or replace function update_user_info()
returns trigger as
$body$
begin
  update user1
    set
        email = new.email,
        first_name = new.first_name,
        last_name = new.last_name,
        pass_word = new.pass_word,
        loc = new.loc
      where new.user_name = user1.user_name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;
create trigger update_user_info_trigger
instead of update on v_overal_info_username
for each row
execute procedure update_user_info();
