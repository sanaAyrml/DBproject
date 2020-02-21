-- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pass123';

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
drop database if exists Prj2;
create DATABASE Prj2;
CREATE DOMAIN TYPE_RES AS TEXT
CHECK(
   VALUE ~ 'Iranian'
OR VALUE ~ 'Italian'
OR VALUE ~ 'Salad'
OR VALUE ~ 'Homemade'
OR VALUE ~ 'Japaneese'
OR VALUE ~ 'Internatinal'
);
CREATE DOMAIN TYPE_FOOD AS TEXT
CHECK(
   VALUE ~ 'Appetizer'
OR VALUE ~ 'Main'
OR VALUE ~ 'Pizza'
OR VALUE ~ 'Burgur'
OR VALUE ~ 'Salad'
OR VALUE ~ 'drinks'
);

CREATE DOMAIN TYPE_BACKUP AS TEXT
CHECK(
   VALUE ~ 'costumor'
OR VALUE ~ 'cyclist'
);

CREATE DOMAIN TYPE_PAYMENT AS TEXT
CHECK(
   VALUE ~ 'CASH'
OR VALUE ~ 'CREDIT'
);

CREATE DOMAIN STATE AS TEXT
CHECK(
    VALUE ~ 'NO'
    OR VALUE ~ 'PENDING'
    OR VALUE ~ 'OK'
);

CREATE DOMAIN CHOSEN AS TEXT
CHECK(
   VALUE ~ 'YES'
OR VALUE ~ 'No'
);

CREATE DOMAIN address_dom AS TEXT;

CREATE DOMAIN score_dom AS DEC(4,2) DEFAULT 0.00 CONSTRAINT giving_score CHECK (VALUE BETWEEN 0 AND 10);

CREATE DOMAIN price_dom AS DEC(10,2) DEFAULT 0.00 CONSTRAINT giving_PRICE CHECK (VALUE >= 0);

CREATE DOMAIN discount_dom AS DEC(5,2) DEFAULT 0.00 CONSTRAINT giving_DISCOUNT CHECK (VALUE >= 0 AND VALUE <= 100);

CREATE DOMAIN salary_dom AS DEC(10,2) DEFAULT 0.00 CONSTRAINT giving_SALARY CHECK (VALUE >= 0);

CREATE DOMAIN cartnum_dom AS INTEGER DEFAULT 0 CONSTRAINT giving_CARTNUM CHECK (VALUE >= 0);

create domain positive_dec as DEC(10,2) DEFAULT 0.00 CONSTRAINT pos CHECK (VALUE >= 0);

create table restaurant
(name CHAR(8) NOT NULL,
coverageZone INTEGER DEFAULT 20,
credit INTEGER DEFAULT 0,
type TYPE_RES,
address address_dom,
score score_dom,
loc_x positive_dec,
loc_y positive_dec,
primary key (name));

create table food
(name CHAR(8) NOT NULL,
type TYPE_FOOD,
primary key (name));


create table menu
(food_name CHAR(8) NOT NULL,
restaurant_name CHAR(8) NOT NULL,
Price price_dom,
Discount discount_dom,
primary key (food_name,restaurant_name),
foreign key (restaurant_name) REFERENCES restaurant(name),
foreign key (food_name) REFERENCES food(name));

create table back_up
(national_code CHAR(8) NOT NULL,
first_name CHAR(8) NOT NULL,
last_name CHAR(8) NOT NULL,
address address_dom,
start_work_time time,
end_work_time time,
type TYPE_BACKUP,
score score_dom,
salary salary_dom,
primary key (national_code));



create table user1
(user_name CHAR(8) NOT NULL,
first_name CHAR(8) NOT NULL,
last_name CHAR(8) NOT NULL,
email varchar(20),
credit INTEGER default 0,
check ( credit >= 0 ),
national_code VARCHAR(10) NOT NULL DEFAULT(0000000000)UNIQUE,
pass_word VARCHAR(8) NOT NULL DEFAULT(00000000),
primary key (user_name));

create table comment_user_rest
(user_name CHAR(8) NOT NULL,
restaurant_name CHAR(8) NOT NULL,
comment TEXT,
primary key (user_name,restaurant_name,comment),
foreign key (user_name) REFERENCES user1(user_name),
foreign key (restaurant_name) REFERENCES food(name));

create table deliver_man
(user_name CHAR(8) NOT NULL,
motorcycle_plaque CHAR(8) NOT NULL,
score score_dom,
loc_x positive_dec,
loc_y positive_dec,
primary key (user_name),
foreign key (user_name) REFERENCES user1(user_name));

create table costumer(
  user_name CHAR(8) NOT NULL,
  address address_dom,
  loc_x positive_dec,
  loc_y positive_dec,
  chosen_address CHOSEN default 'NO',
  primary key (user_name,address),
  foreign key (user_name) REFERENCES user1(user_name)
);
create table deliver_man_call_backup
(user_name CHAR(8) NOT NULL,
national_code VARCHAR(10) NOT NULL DEFAULT(0000000000),
score score_dom,
primary key (user_name, national_code),
foreign key (user_name) REFERENCES deliver_man(user_name),
foreign key (national_code) REFERENCES back_up(national_code));

create table costumer_call_backup
(user_name CHAR(8) NOT NULL,
national_code VARCHAR(10) NOT NULL DEFAULT(0000000000),
score score_dom,
primary key (user_name,national_code),
foreign key (user_name) REFERENCES user1(user_name),
foreign key (national_code) REFERENCES back_up(national_code));


create table cart1
(user_name CHAR(8) NOT NULL,
cart_num cartnum_dom,
restaurant_name CHAR(8) NOT NULL,
total_price price_dom,
accepted STATE default 'NO',
accepted_del CHAR(8) default NULL,
primary key (user_name,cart_num),
foreign key (user_name) REFERENCES user1(user_name),
foreign key (restaurant_name) REFERENCES restaurant(name));

create table cart2
(user_name CHAR(8) NOT NULL,
cart_num cartnum_dom,
food_name CHAR(8) NOT NULL,
food_num INTEGER NOT NULL,
check ( food_num >= 1 ),
primary key (food_name,user_name,cart_num),
foreign key (food_name) REFERENCES food(name),
foreign key (user_name,cart_num) REFERENCES cart1(user_name,cart_num));

create table pay
(user_name CHAR(8) NOT NULL,
cart_num cartnum_dom,
delivery_user_name CHAR(8) NOT NULL,
restaurant_name CHAR(8) NOT NULL,
payment_type TYPE_PAYMENT,
delivery_cost INTEGER,
res_score score_dom,
dm_score score_dom,
check ( delivery_cost >= 0 ),
primary key (user_name,cart_num,delivery_user_name,restaurant_name),
foreign key (user_name,cart_num) REFERENCES cart1(user_name,cart_num),
foreign key (delivery_user_name) REFERENCES deliver_man(user_name),
foreign key (restaurant_name) REFERENCES restaurant(name));

create table increase_user_credit(
  user_name CHAR(8) NOT NULL,
  amount integer,
  year integer,
  month integer,
  day integer,
  hour integer,
  check ( year >= 0 and year <= 99),
  check ( month >= 1 and month <=12 ),
  check ( day >= 1 and day <= 30 ),
  check ( hour >= 0 and hour <=24 ),
  check ( amount >= 0 ),
  primary key (user_name, year, month, day, hour),
  foreign key (user_name) references user1(user_name)
);

