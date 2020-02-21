create view v_neighbourhood_restaurants_score(restaurant_name, restaurant_score, restaurant_address, restaurant_type, distance)
    as select restaurant.name, restaurant.score, restaurant.address, restaurant.type, power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y - costumer.loc_y, 2) as distance from restaurant , costumer
    where  power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y-costumer.loc_y, 2) <= power(restaurant.coverageZone, 2)
    and costumer.chosen_address = 'YES' and costumer.user_name = 'asghar'
    order by restaurant.score;


create view v_neighbourhood_restaurants_distance(restaurant_name, restaurant_score, restaurant_address, restaurant_type, distance)
    as select restaurant.name, restaurant.score, restaurant.address, restaurant.type, power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y - costumer.loc_y, 2) as distance from restaurant , costumer
    where  power(restaurant.loc_x-costumer.loc_x, 2) + power(restaurant.loc_y-costumer.loc_y, 2) <= power(restaurant.coverageZone, 2)
    and costumer.chosen_address = 'YES' and costumer.user_name = 'asghar'
    order by 5;

create view v_carts(user_name, cart_num, restaurant_name, food_name, food_num, price)
    as select cart1.user_name, cart1.cart_num, cart1.restaurant_name, cart2.food_name, cart2.food_num, menu.price * (100 - menu.discount) *cart2.food_num / 100
    from cart1, cart2 , menu
    where cart1.cart_num = cart2.cart_num and cart1.user_name = cart2.user_name and menu.restaurant_name = cart1.restaurant_name  and cart2.food_name = menu.food_name and cart1.user_name = 'asghar'
    order by cart1.cart_num;

create view v_uncompleted_carts(cart_num, restaurant_name, food_price)
    as select cart1.cart_num, cart1.restaurant_name, cart1.total_price from cart1
    where  cart1.accepted = 'NO' and cart1.user_name = 'asghar';

create view v_payments(user_name, cart_num, delivery_user_name, restaurant_name, payment_type, delivery_cost, res_score, dm_score, food_cost)
    as select pay.user_name, pay.cart_num, pay.delivery_user_name, pay.restaurant_name, pay.payment_type, pay.delivery_cost, pay.res_score, pay.dm_score, cart1.total_price from cart1, pay
    where cart1.cart_num = pay.cart_num and cart1.user_name = pay.user_name and cart1.user_name = 'asghar';

create view v_increase_credit(user_name, year, month, day, hour, amount)
as select user_name, year, month, day, hour, amount from increase_user_credit
where user_name = 'asghar';

create view v_overal_info_username(user_name, first_name, last_name, email, pass_word, credit)
    as select user1.user_name, user1.first_name, user1.last_name,user1.email , user1.pass_word, user1.credit from user1
    where user1.user_name = 'asghar';

create view ز(user_name, address, loc_x, loc_y, chosen_address)
  as select costumer.user_name, costumer.address, costumer.loc_x, costumer.loc_y, costumer.chosen_address from costumer
    where costumer.user_name = 'asghar';

create view v_profile_delivery(user_name, first_name, last_name, email, motorcyclr_plaque, pass_word, loc_x, loc_y)
    as select user1.user_name, user1.first_name, user1.last_name, user1.email , deliver_man.motorcycle_plaque, user1.pass_word, deliver_man.loc_x, deliver_man.loc_y from user1, deliver_man
    where deliver_man.user_name = user1.user_name and deliver_man.user_name = 'asghar';
