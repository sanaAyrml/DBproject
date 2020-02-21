import time
from random import randint

import binary as binary
import mysql.connector
import psycopg2

db = psycopg2.connect(host='127.0.0.1', database='prj7', user='postgres')
db.rollback()
cursor = db.cursor()


# query = "create view v_carts(cart_num, restaurant_name, food_name) as select cart1.cart_num, cart1.restaurant_name, cart2.food_name from cart1, cart2 where cart1.cart_num = cart2.cart_num and cart1.user_name = cart2.user_name and cart1.user_name = '1';"
# cursor.execute(query)
# db.commit()
def start():
    command = raw_input()
    if command == "Create account":
        return C()
    elif command == "Login account":
        return B()


def B():
    command = raw_input()
    if command == "delivery":
        B1()
    elif command == "costumer":
        B2()
    return B()


def C():
    command = raw_input()
    if command == "delivery":
        C1()
    elif command == "costumer":
        C2()
    return C()


def B1():
    print("enter in right order username, password:")
    print("username:")
    username = raw_input()
    print("password:")
    pw = raw_input()
    if username != "Back":
        query = "SELECT * From user1 where user1.user_name = '" + username + "' and user1.pass_word = '" + pw + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 1:
            D(username)
        else:
            print"wrong username or password"
            return B1()
        return B1()
    elif username == "Back":
        return B()
    else:
        return B1()


def B2():
    print("enter in right order username, password:")
    print("username:")
    username = raw_input()
    print("password:")
    pw = raw_input()
    if username != "Back":
        query = "SELECT * From user1 where user1.user_name = '" + username + "' and user1.pass_word = '" + pw + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 1:
            E(username)
        else:
            print"wrong username or password"
            return B2()
        return B2()
    elif username == "Back":
        return B()
    else:
        return B2()


def C1():
    print(
        "enter in right order username, first name, last name, email, national code, location, password, motorcycle plaque:")
    print("enter in right order: ")
    print("username:")
    username = raw_input()
    if username != "Back":
        query = "SELECT * From user1 where user1.user_name = '" + username + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            print("first name:")
            firstname = raw_input()
            print("last name:")
            lastname = raw_input()
            print("email:")
            email = raw_input()
            print("NC:")
            NC = raw_input()
            print("PW:")
            PW = raw_input()
            query = "INSERT INTO user1(user_name, first_name, last_name, email, credit, national_code, pass_word) VALUES ('" + username + "', '" + firstname + "', '" + lastname + "', '" + email + "' , 0 , '" + NC + "', '" + PW + "')"
            cursor.execute(query)
            db.commit()
            print("motorcycle_plaque:")
            mp = raw_input()
            print("location_x:")
            loc_x = raw_input()
            print("location_y:")
            loc_y = raw_input()
            query = "INSERT INTO deliver_man(user_name, motorcycle_plaque, score, loc_x, loc_y) VALUES ('" + username + "', '" + mp + "', 0," + loc_x + "," + loc_y + ")"
            cursor.execute(query)
            db.commit()
            query = "create view v_profile_delivery_" + username + "(user_name, first_name, last_name, email,motorcyclr_plaque,  pass_word,  loc_x, loc_y) as select user1.user_name, user1.first_name, user1.last_name,user1.email , deliver_man.motorcycle_plaque, user1.pass_word, deliver_man.loc_x, deliver_man.loc_y from user1, deliver_man where deliver_man.user_name = user1.user_name and deliver_man.user_name = '" + username + "';"
            cursor.execute(query)
            db.commit()
            return D(username)
        else:
            print("usernam already exists")
            return C1()
    elif username == "Back":
        return C()
    else:
        return C1()


def C2():
    print("enter in right order: ")
    print("username:")
    username = raw_input()
    if username != "Back":
        query = "SELECT * From user1 where user_name = '" + username + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            print("first name:")
            firstname = raw_input()
            print("last name:")
            lastname = raw_input()
            print("email:")
            email = raw_input()
            print("NC:")
            NC = raw_input()
            print("PW:")
            PW = raw_input()
            query = "INSERT INTO user1(user_name, first_name, last_name, email, credit, national_code, pass_word) VALUES ('" + username + "', '" + firstname + "', '" + lastname + "', '" + email + "' , 0 , '" + NC + "', '" + PW + "')"
            cursor.execute(query)
            db.commit()
            print("address:")
            add = raw_input()
            print("location_x:")
            loc_x = raw_input()
            print("location_y:")
            loc_y = raw_input()
            query = "insert into costumer(user_name, address, loc_x, loc_y) values ('" + username + "', '"+ add + "', "+ loc_x + ","+loc_y+")"
            cursor.execute(query)
            db.commit()
            query = "create view v_neighbourhood_restaurants_score_" + username + "(restaurant_name, restaurant_score, restaurant_address, restaurant_type, distance) as select restaurant.name, restaurant.score, restaurant.address, restaurant.type, power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y - costumer.loc_y, 2) as distance from restaurant , costumer where  power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y-costumer.loc_y, 2) <= power(restaurant.coverageZone, 2)  and costumer.chosen_address = 'YES' and costumer.user_name = '" + username + "' order by restaurant.score;"
            cursor.execute(query)
            db.commit()
            query = "create view v_neighbourhood_restaurants_distance_" + username + "(restaurant_name, restaurant_score, restaurant_address, restaurant_type, distance) as select restaurant.name, restaurant.score, restaurant.address, restaurant.type, power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y - costumer.loc_y, 2) as distance from restaurant , costumer where  power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y-costumer.loc_y, 2) <= power(restaurant.coverageZone, 2) and costumer.chosen_address = 'YES' and costumer.user_name = '" + username + "' order by 5;"
            cursor.execute(query)
            db.commit()
            query = "create view v_carts_" + username + "(user_name, cart_num, restaurant_name, food_name, food_num, price) as select cart1.user_name, cart1.cart_num, cart1.restaurant_name, cart2.food_name, cart2.food_num, menu.price * (100 - menu.discount) *cart2.food_num / 100 from cart1, cart2 , menu where cart1.cart_num = cart2.cart_num and cart1.user_name = cart2.user_name and menu.restaurant_name = cart1.restaurant_name  and cart2.food_name = menu.food_name and cart1.user_name = '" + username + "' order by cart1.cart_num;"
            cursor.execute(query)
            db.commit()
            query = "create view v_uncompleted_carts_" + username + "(cart_num, restaurant_name, food_price) as select cart1.cart_num, cart1.restaurant_name, cart1.total_price from cart1 where  cart1.accepted = 'NO' and cart1.user_name = '" + username + "';"
            cursor.execute(query)
            db.commit()
            query = "create view v_payments_" + username + "(user_name, cart_num, delivery_user_name, restaurant_name, payment_type, delivery_cost, res_score, dm_score, food_cost) as select pay.user_name, pay.cart_num, pay.delivery_user_name, pay.restaurant_name, pay.payment_type, pay.delivery_cost, pay.res_score, pay.dm_score, cart1.total_price from cart1, pay where cart1.cart_num = pay.cart_num and cart1.user_name = pay.user_name and cart1.user_name ='" + username + "';"
            cursor.execute(query)
            db.commit()
            query = "create view v_increase_credit_" + username + "(user_name, year, month, day, hour, amount) as select user_name, year, month, day, hour, amount from increase_user_credit where user_name = '" + username + "';"
            cursor.execute(query)
            db.commit()
            query = "create view v_overal_info_username_" + username + "(user_name, first_name, last_name, email, pass_word, credit) as select user1.user_name, user1.first_name, user1.last_name,user1.email , user1.pass_word, user1.credit from user1 where user1.user_name = '" + username + "';"
            cursor.execute(query)
            db.commit()
            query = "create view v_costumer_address_" + username + "(user_name, address, loc_x, loc_y, chosen_address) as select costumer.user_name, costumer.address, costumer.loc_x, costumer.loc_y, costumer.chosen_address from costumer where costumer.user_name = '" + username + "';"
            cursor.execute(query)
            db.commit()
            query = """ create or replace function inc_credit_"""+username+"""()
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
                        cost 100; """
            cursor.execute(query)
            db.commit()
            query = """create trigger inc_credit_trigger_"""+username+"""
                        instead of insert on v_increase_credit_"""+username+"""
                        for each row
                        execute procedure inc_credit_"""+username+"""(); """
            cursor.execute(query)
            db.commit()

            query = """ create or replace function credit_transfer_"""+username+"""()
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
"""
            cursor.execute(query)
            db.commit()
            query = """create trigger credit_payment_trigger_"""+username+"""
instead of insert on v_payments_"""+username+"""
for each row
execute procedure credit_transfer_"""+username+"""();"""
            cursor.execute(query)
            db.commit()

            query = """ create or replace function update_cart_"""+username+"""()
returns trigger as
$body$
begin
  if ((new.user_name, new.cart_num) not in (select user_name, cart_num from cart1)) then
    insert into cart1 values (new.user_name, new.cart_num, new.restaurant_name, 0, 'NO', null);
  end if;
  if ((new.user_name, new.cart_num, new.food_name) not in (select user_name, cart_num, food_name from cart2)) then
      insert into cart2 values (new.user_name, new.cart_num, new.food_name, new.food_num);
      else
      update cart2 set food_num = cart2.food_num + new.food_num where
              cart2.user_name = new.user_name and cart2.cart_num = new.cart_num and cart2.food_name = new.food_name;
  end if;
  update cart1
    set total_price = (select total_price from cart1 where cart1.cart_num = new.cart_num and cart1.user_name = new.user_name) +
                      (select menu.price * (100 - menu.discount) * new.food_num / 100 from menu where menu.restaurant_name = new.restaurant_name and menu.food_name = new.food_name)
      where new.cart_num = cart1.cart_num and cart1.user_name = new.user_name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100; """
            cursor.execute(query)
            db.commit()
            query = """create trigger update_cart_trigger_"""+username+"""
instead of insert on v_carts_"""+username+"""
for each row
execute procedure update_cart_"""+username+"""();"""
            cursor.execute(query)
            db.commit()

            query = """ create or replace function cal_dm_score_"""+username+"""()
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
cost 100; """
            cursor.execute(query)
            db.commit()
            query = """create trigger update_dm_score_trigger_"""+username+"""
instead of update on v_payments_"""+username+"""
for each row
execute procedure cal_dm_score_"""+username+"""(); """
            cursor.execute(query)
            db.commit()

            query = """ create or replace function cal_res_score_"""+username+"""()
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
cost 100; """
            cursor.execute(query)
            db.commit()
            query = """create trigger update_res_score_trigger_"""+username+"""
instead of update on v_payments_"""+username+"""
for each row
execute procedure cal_res_score_"""+username+"""();"""
            cursor.execute(query)
            db.commit()

            query = """ create or replace function update_user_info_"""+username+"""()
returns trigger as
$body$
begin
  update user1
    set
        email = new.email,
        first_name = new.first_name,
        last_name = new.last_name,
        pass_word = new.pass_word
      where new.user_name = user1.user_name;
  return new;
end;
$body$
Language plpgsql VOLATILE
cost 100; """
            cursor.execute(query)
            db.commit()
            query = """create trigger update_user_info_trigger_"""+username+"""
instead of update on v_overal_info_username_"""+username+"""
for each row
execute procedure update_user_info_"""+username+"""();"""
            cursor.execute(query)
            db.commit()

            return E(username)
        else:
            print("usernam already exists")
            return C2()
    elif username == "Back":
        return C()
    else:
        return C2()


def E(username):
    print("Choose an action:")
    print("1- profile info")
    print("2- neighbourhood restaurants :")
    print("3- uncompleted carts:")
    print("4- purchase history:")
    print("5- increase credit #AMOUNT :")
    print("6- call backup:")
    print("7- add address:")
    print("8- choose address:")
    entery = list(raw_input().split(" "))
    if entery[0] != "Back":
        if entery[0] == "1-":
            return F(username)
        elif entery[0] == "2-":
            return G(username)
        elif entery[0] == "3-":
            return H(username)
        elif entery[0] == "4-":
            return I(username)
        elif entery[0] == "5-":
            query = "Insert into v_increase_credit_"+username+"(user_name, year, month, day, hour, amount) values('"+username+"',"+str(time.localtime(time.time()).tm_year)+","+str(time.localtime(time.time()).tm_mon)+","+str(time.localtime(time.time()).tm_mday)+","+str(time.localtime(time.time()).tm_hour)+","+entery[3]+")"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "6-":
            query = "SELECT * From back_up where back_up.type = 'costumor'"
            cursor.execute(query)
            result = cursor.fetchall()
            r = randint(0, len(result))
            entery = raw_input()
            query = "INSERT INTO costumer_call_backup VALUES ('" + username + "', '" + result[r][0] + "', '" + entery + "')"
            cursor.execute(query)
            db.commit()
            return E(username)
            pass
        elif entery[0] == "7-":
            entery = list(raw_input().split(" "))
            query = "INSERT INTO v_costumer_address_"+ username +"(user_name, address, loc_x, loc_y) VALUES ('" + username + "', '" + entery[0] + "'," + entery[1] + ","+entery[2]+")"
            cursor.execute(query)
            db.commit()
            return E(username)
            pass
        else:
            query = "SELECT * FROM v_costumer_address_"+username
            cursor.execute(query)
            result = cursor.fetchall()
            print("addresses:")
            for i in range(len(result)):
                print (result[i][1])
            address = raw_input()
            query = "UPDATE v_costumer_address_"+ username +" set chosen_address = 'YES' where address = '" + address + "'"
            cursor.execute(query)
            db.commit()
            return E(username)
    elif entery[0] == "Back":
        return start()
    else:
        return E(username)


def F(username):
    print ("Profile info:")
    query = "SELECT * From v_overal_info_username_"+username
    cursor.execute(query)
    result = cursor.fetchall()
    print ("user name: " + result[0][0])
    print ("first name: " + result[0][1])
    print ("last name: " + result[0][2])
    print ("email: " + result[0][3])
    print ("password: " + result[0][4])
    print ("credit: " + str(result[0][5]))
    print("addresses:")
    for i in range(len(result)):
        print(result[i][3])
    print("Choose an action:")
    print("1- edit email:")
    print("2- edit password:")
    print("3- edit first name")
    print("4- edit last name :")
    entery = list(raw_input().split(" "))
    if entery[0] != "Back":
        if entery[0] == "1-":
            email = raw_input()
            query = "UPDATE v_overal_info_username_"+username +" SET email = ' " + email + "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "2-":
            password = raw_input()
            query = "UPDATE v_overal_info_username_"+username +" SET pass_word = '" + password+ "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "3-":
            first = raw_input()
            query = "UPDATE v_overal_info_username_"+username +" SET first_name = ' " + first + "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "4-":
            last = raw_input()
            query = "UPDATE v_overal_info_username_"+username +" SET last_name = ' " + last + " '"
            cursor.execute(query)
            db.commit()
        else:
            return F(username)
        return F(username)
    elif entery[0] == "Back":
        return E(username)
    else:
        return F(username)


def G(username):
    print ("show restaurant in order:")
    query = "SELECT * From v_neighbourhood_restaurants_score_"+username
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print (i)
        # print ("restaurant name: " + i[0] + "restaurant score: " + i[1] + "restaurant address: " + i[2] +
        #        "restaurant type: " + i[3])
    print("Choose an action:")
    print("1- add filter:")
    print("2- enter restaurant name :")
    entery = list(raw_input().split(" "))
    if entery[0] != "back":
        if entery[0] == "1-":
            type = entery[3]
            G1(username, type)
        elif entery[0] == "2-":
            entery = raw_input()
            query = "SELECT * From v_neighbourhood_restaurants_score_"+username+" where restaurant_name = '" + entery + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) > 0:
                J(username, entery)
            else:
                G(username)
        else:
            return G(username)
        return G(username)
    elif entery[0] == "back":
        return E(username)
    else:
        return G(username)


def G1(username, type):
    print ("show restaurant in order:")
    query = "SELECT * From v_neighbourhood_restaurants_score_"+username+" where restaurant_type = '" + type + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result():
        print ("restaurant name: " + i[0] + "restaurant score: " + i[1] + "restaurant address: " + i[2] +
               "restaurant type: " + i[3])
    print("Choose an action:")
    print("1- delete filter:")
    print("2- enter restaurant name :")
    entery = list(raw_input().split(" "))
    if entery[0] != "back":
        if entery[0] == "1-":
            G(username)
        elif entery[0] == "2-":
            entery = raw_input()
            query = "SELECT * From v_neighbourhood_restaurants_score_"+username+" where restaurant_name = '" + entery + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) > 0:
                J(username, entery)
            else:
                G1(username,type)
        else:
            return G1(username,type)
        return G1(username,type)
    elif entery[0] == "back":
        return G(username)
    else:
        return G1(username,type)


def pending(username, restauran, tot_price, cartnum):
    entery = raw_input()
    print ("waiting")
    if entery == "check":
        print ("checked")
        query = "SELECT * From  cart1 where  user_name = '" + username + "' and cart_num = " + str(cartnum)
        cursor.execute(query)
        result = cursor.fetchall()
        if result[0][4] == 'OK':
            return K(username, restauran, result[0][5], cartnum, tot_price)
        else:
            return pending(username, restauran, tot_price, cartnum)
    elif entery == "exit":
        print ("exit")
        query = "update cart1 set accepted = 'NO' where user_name = '" + username + "' and cart_num = " + str(cartnum)
        cursor.execute(query)
        db.commit()
        return G(username)
    else:
        return pending(username, restauran, tot_price, cartnum)


def H(username):
    print ("show uncompelet carts:")
    query = "SELECT * From  v_uncompleted_carts_"+username
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print (i)
    print("Choose an action:")
    print("1- pay:")
    entery = list(raw_input().split(" "))
    if entery[0] != "back":
        if entery[0] == "1-":
            query = "SELECT * From  v_uncompleted_carts_"+username+" where cart_num = '" + entery[2] + "'"
            cursor.execute(query)
            result = cursor.fetchall()
            query = "update cart1 set accepted = 'PENDING' where user_name = '" + username + "' and cart_num = " + entery[2]
            cursor.execute(query)
            db.commit()
            return pending(username, result[0][0], result[0][1], result[0][2])
    elif entery[0] == "back":
        return E(username)
    else:
        return H(username)


def I(username):
    print ("show history:")
    query = "SELECT * From  v_payments_"+username
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result():
        print ("restaurant name: " + i[3] + "payment type: " + i[4] + "deliveryman username: " + i[2] +
               "deliveryman_score: " + i[7] + "restaurant_score: " + i[6] + "cart_price: " + i[8])
    print("Choose an action:")
    print("1- enter comment #restaurant_name:")
    entery = list(raw_input().split(" "))
    if entery[0] != "back":
        if entery[0] != "1-":
            comment = raw_input()
            query = "INSERT INTO comment_user_rest VALUES ('" + username + "', '" + entery[3] + "', '" + comment + "')"
            cursor.execute(query)
            db.commit()
            print ("comment inserted")
            return I(username)
        else:
            return I(username)
    elif entery[0] == "back":
        return E(username)
    else:
        return I(username)


def N(username, restaurant_name):
    print ("show comments:")
    query = "SELECT * From  comment_user_rest where  comment_user_rest.restaurant_name = '" + restaurant_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result)>0:
        for i in result():
            print ("user name: " + i[0] + "comment: " + i[2])
    entery = list(raw_input().split(" "))
    if entery[0] == "back":
        return E(username)
    else:
        return I(username)


def J(username, restauran):
    print ("show menu and price and discount:")
    query = "SELECT * From menu where restaurant_name = '" + restauran + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i[0], i[2], i[3])
    print("Choose an action:")
    print("1- start choosing food:")
    print("2- comments:")
    print("back:")
    entery = list(raw_input().split(" "))
    if entery[0] == "1-":
        query = "SELECT cart_num From v_carts_"+ username
        cursor.execute(query)
        result = cursor.fetchall()
        array = []
        for i in result:
            array.append(i[0])
        if len(result)>0:
            print result
            maximum = max(array)
        else:
            maximum = 0
        return Z(username, restauran, maximum + 1)
        pass
    elif entery[0] == "2-":
        N(username, restauran)
    elif entery[0] == "back":
        G(username)
        pass
    else:
        return J(username, restauran)


def Z(username, restauran, cartnum):
    print ("show total price:")
    query = "SELECT price From v_carts_"+ username +" where cart_num = "+ str(cartnum)
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result)>0:
        print("TOTAL PRICE:" + str(result[0][0]))
    else:
        print ("TOTAL PRICE: 0")
    print("Choose an action:")
    print("1- choose food:")
    print("2- pay:")
    print("back:")
    entery = list(raw_input().split(" "))
    if entery[0] == "1-":
        foodname = raw_input()
        number = raw_input()
        # query = "SELECT * From cart2 where cart2.user_name = '" + username + "' and cart2.cart_num = '" + cartnum + "' and cart2.food_name = '" + foodname + "'"
        # cursor.execute(query)
        # result = cursor.fetchall()
        # if len(result) > 0:
        #     query = "UPDATE cart2 set cart2.food_num = cart2.food_num + 1 where cart2.user_name = '" + username + "' and cart2.cart_num = '" + cartnum + "' and cart2.food_name = '" + foodname + "'"
        #     cursor.execute(query)
        #     db.commit()
        # else:
        #     query = "INSERT INTO cart2  values('" + username + "' , '" + cartnum + "' ,'" + foodname + "',1)"
        #     cursor.execute(query)
        #     db.commit()
        query = "insert into v_carts_"+username+"(user_name, cart_num, restaurant_name, food_name, food_num) values ('"+username+"','"+str(cartnum)+"','"+restauran+"','"+foodname+"',"+number+")"
        cursor.execute(query)
        db.commit()
        Z(username, restauran, cartnum)
    # elif entery[0] == "2-":
    #     foodname = raw_input()
    #     query = "SELECT * From cart2 where cart2.user_name = '" + username + "' and cart2.cart_num = '" + cartnum + "' and cart2.food_name = '" + foodname + "'"
    #     cursor.execute(query)
    #     result = cursor.fetchall()
    #     if len(result) > 1:
    #         query = "UPDATE cart2 set cart2.food_num = cart2.food_num - 1 where cart2.user_name = '" + username + "' and cart2.cart_num = '" + cartnum + "' and cart2.food_name = '" + foodname + "'"
    #         cursor.execute(query)
    #         db.commit()
    #     elif len(result) == 1:
    #         query = "DELETE From cart2 where cart2.user_name = '" + username + "' and cart2.cart_num = '" + cartnum + "' and cart2.food_name = '" + foodname + "'"
    #         cursor.execute(query)
    #         db.commit()
    #     else:
    #         print("NO SUCH A FOOD")
    #     return Z(username, restauran, cartnum)
    #     pass
    elif entery[0] == "2-":
        tot_price = result[0][0]
        query = "update cart1 set accepted = 'PENDING' where user_name = '"+username+"' and cart_num = " + str(cartnum)
        cursor.execute(query)
        db.commit()
        return pending(username, restauran, tot_price, cartnum)
        pass
    elif entery[0] == "back":
        J(username, restauran)
        pass
    else:
        return Z(username, restauran, cartnum)


def K(username, restauran, delivery_name, cart_num, tot_price):
    print("Choose an action:")
    print("1- cash pay:")
    print("2- credit pay: ")
    print("back:")
    entery = list(raw_input().split(" "))
    if entery[0] == "1-":
        print ("GIVE SCORE:")
        print ("restauran")
        res_score = raw_input()
        print ("delivery man")
        dm_score = raw_input()
        query = "INSERT INTO v_pay_"+username+"(user_name, cart_num, delivery_user_name, restaurant_name, payment_type, delivery_cost, res_score, dm_score, food_cost) VALUES ('" + username + "', '" + cart_num + "', '" + delivery_name + "', '" + restauran + "', 'CASH', 10, " + res_score + ", " + dm_score + ")"
        cursor.execute(query)
        db.commit()
        return G(username)
    elif entery[0] == "2-":
        print ("GIVE SCORE:")
        print ("restauran")
        res_score = raw_input()
        print ("delivery man")
        dm_score = raw_input()
        query = "INSERT INTO v_pay_" + username + "(user_name, cart_num, delivery_user_name, restaurant_name, payment_type, delivery_cost, res_score, dm_score, food_cost) VALUES ('" + username + "', '" + cart_num + "', '" + delivery_name + "', '" + restauran + "', 'CASH', 10, " + res_score + ", " + dm_score + ")"
        cursor.execute(query)
        db.commit()
        return G(username)
    elif entery[0] == "back":
        return G(username)
        pass
    else:
        return K(username, restauran, delivery_name, cart_num, tot_price)


def P(username):
    print ("Profile info:")
    query = "SELECT * From v_profile_delivery_"+username+" where user_name = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    print ("user name: " + result[0][0])
    print ("first name: " + result[0][1])
    print ("last name: " + result[0][2])
    print ("email: " + result[0][4])
    print ("motor cycle plaque: " + result[0][5])
    print("Choose an action:")
    print("1- edit email:")
    print("2- edit password:")
    print("3- edit first name")
    print("4- edit last name :")
    entery = list(raw_input().split(" "))
    if entery[0] != "Back":
        if entery[0] == "1-":
            email = raw_input()
            query = "UPDATE v_profile_delivery_"+username +" SET email = ' " + email + "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "2-":
            password = raw_input()
            query = "UPDATE v_profile_delivery_"+username +" SET pass_word = '" + password+ "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "3-":
            first = raw_input()
            query = "UPDATE v_profile_delivery_"+username +" SET first_name = ' " + first + "'"
            cursor.execute(query)
            db.commit()
        elif entery[0] == "4-":
            last = raw_input()
            query = "UPDATE v_profile_delivery_"+username +" SET last_name = ' " + last + " '"
            cursor.execute(query)
            db.commit()
        else:
            return F(username)
        return P(username)
    elif entery[0] == "Back":
        return D(username)
    else:
        return P(username)


def Q(username):
    query = "SELECT * From cart1 where accepted = 'PENDING'"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print (i[0], i[1])
    entery = list(raw_input().split())
    if entery[0] != "Back":
        query = "UPDATE cart1 set accepted = 'OK' where cart1.user_name = '" + \
                entery[0] + "' and cart1.cart_num = " + entery[1]
        cursor.execute(query)
        db.commit()
        query = "UPDATE cart1 set accepted_del = '" + username + "' where cart1.user_name = '" + \
                entery[0] + "' and cart1.cart_num = " + entery[1]
        cursor.execute(query)
        db.commit()
        return D(username)
    elif entery[0] == "Back":
        return D(username)
    else:
        return Q(username)


def D(username):
    print("Choose an action:")
    print("1- profile info")
    print("2- call backup:")
    print("3- show requests:")
    entery = list(raw_input().split(" "))
    if entery[0] != "Back":
        if entery[0] == "1-":
            return P(username)
        elif entery[0] == "2-":
            query = "SELECT * From back_up where back_up.type = 'cyclist'"
            cursor.execute(query)
            result = cursor.fetchall()
            r = randint(0, len(result))
            entery = raw_input()
            query = "INSERT INTO costumer_call_backup VALUES ('" + username + "', '" + result[r][
                0] + "', '" + entery + "')"
            cursor.execute(query)
            db.commit()
            return D(username)
        elif entery[0] == "3-":
            return Q(username)
            pass
        else:
            return D(username)
    elif entery[0] == "Back":
        return start()
    else:
        return D(username)


print("WELCOME Create account or Login accoun")
start()
