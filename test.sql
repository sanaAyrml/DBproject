insert into restaurant values ('rosana', 10, 0, 'Italian', 'esf-mardavij', 0, 2, 3);
insert into restaurant values ('almahdi', 20, 0, 'Iranian', 'teh-tarasht', 0, 200, 300);
insert into restaurant values ('sagpaz', 10, 0, 'Iranian', 'ghasem-jasem', 0, 8, 4);

insert into food values ('meygo', 'Main');
insert into food values ('magia', 'Pizza');

insert into menu values ('meygo', 'rosana', 40, 10);
insert into menu values ('magia', 'rosana', 30, 20);

insert into user1 values ('asghar', 'asgh', 'farhadi', 'asfarh@yahoo.com', 0, 1234, 111);
insert into user1 values ('akbar001', 'akbar', 'farhadi', 'akbh@yahoo.com', 0, 5678, 222);
insert into deliver_man values ('akbar001', '12345678', 0, 34, 56);
insert into user1 values ('ali002', 'ali', 'rabie', 'akrb@yahoo.com', 0, 0987, 222);
insert into deliver_man values ('ali002', '567894', 0, 34, 56);

-- check trigger change_address
insert into costumer values ('asghar', 'tarasht', 5, 1, 'YES');
insert into costumer values ('asghar', 'ekbatan', 190, 300, 'YES');
select * from costumer;
update costumer set chosen_address = 'YES' where address = 'tarasht';
select * from costumer;

-- check update_cart
insert into v_carts values ('asghar', 1, 'rosana', 'magia', 3, null);
insert into v_carts values ('asghar', 1, 'rosana', 'meygo', 2, null);
insert into v_carts values ('asghar', 2, 'rosana', 'magia', 4, null);
select * from cart1;
select * from cart2;
select * from v_carts;

-- check increase_credit
insert into v_increase_credit values ('asghar', 79, 7, 15, 3, 300);
select * from v_increase_credit;
select * from user1;

-- check credit_transfer
insert into v_payments values ('asghar', 2, 'akbar001', 'rosana', 'CREDIT', 10, 7, 3, null);
select * from pay;
insert into v_payments values ('asghar', 1, 'akbar001', 'rosana', 'CREDIT', 10, 5, 1, null);
select * from deliver_man;

insert into v_payments values ('asghar', 2, 'ali002', 'rosana', 'CREDIT', 8, 4, 9, null);
select * from deliver_man;

insert into v_payments values ('asghar', 2, 'ali002', 'rosana', 'CASH', 8, 4, 9, null);
select * from user1;
select * from deliver_man;
select * from restaurant;

-- check costumer call backup trigger
insert into back_up values ('13579', 'maryam', 'mirzai', null, null, null, 'costumor', 0, 90);
insert into user1 values ('glb_tlb', 'golabi', 'talebi', 'glbtlb@yahoo.com', 0, 4321, 9090);
insert into costumer_call_backup values ('glb_tlb', '13579', 9);
insert into costumer_call_backup values ('asghar', '13579', 5);
select * from back_up;

-- check deliver_man call backup trigger
insert into back_up values ('97531', 'brah', 'plah', null, null, null, 'costumor', 0, 100);
insert into deliver_man_call_backup values ('akbar001', '97531', 7);
select * from back_up;

-- update user info
update user1 set email = 'newmail@gmail.com' where user_name = 'glb_tlb';
select * from user1;