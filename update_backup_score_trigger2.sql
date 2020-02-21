create or replace function cal_bu_score2()
returns trigger as
$body$
begin
  update back_up
    set score = (select avg(score) from deliver_man_call_backup
            where new.national_code = deliver_man_call_backup.national_code
            )
      where new.national_code = back_up.national_code;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100;

create trigger update_bu_score_trigger2
after insert on deliver_man_call_backup
for each row
execute procedure cal_bu_score2()