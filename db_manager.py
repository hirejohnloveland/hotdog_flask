from app.blueprints.menu.models import *
from app.blueprints.orders.models import *
from app import db

###############################################
####### Initialization Script #################
###############################################


class Db_Build():

    @staticmethod
    def db_init_all():
        Db_Build.db_init_cat()
        Db_Build.db_init_ing()
        Db_Build.db_init_menu()
        Db_Build.db_init_menu_ingredients()
        Db_Build.db_init_payment_type()
        Db_Build.db_init_order_status()

    @staticmethod
    def db_init_cat():
        cat_list = []
        cat_list.append(Category("Dogs", 1))
        cat_list.append(Category("Sides", 2))
        cat_list.append(Category("Extras", 3))
        cat_list.append(Category("Beverages", 4))
        for cat in cat_list:
            db.session.add(cat)
        db.session.commit()

    @staticmethod
    def db_init_ing():
        ingredients = ["Bacon", "Grilled Peppers", "Onion", "Jalepenos", "Pickle Spear", "Celery Salt",
                       "Green Relish", "Tomatoes", "Mustard", "Bell Peppers", "Ketchup", "Avacado Chunks", "Mayonnaise", "Saurkraut", "French Fries", "Swiss Cheese"]
        for ingredient in ingredients:
            add = Ingredient(ingredient)
            db.session.add(add)
        db.session.commit()

    @staticmethod
    def db_init_menu():
        menu_list = []
        menu_list.append(Menu_Item(
            1, "Tijuana", "Bacon wrapped all beef hot dog with grilled peppers and jalepenos", 8.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616299/HotDogFT/Tijuana_bccwhd.jpg', 2))
        menu_list.append(Menu_Item(
            1, "Chicago", "All Beef hot dog topped with onions, tomatoes, relish, and a pickle spear on a poppy seed bun", 7.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616299/HotDogFT/Chicago_rnnxr7.jpg', 1))
        menu_list.append(Menu_Item(
            1, "Italian", "Deep friend doggy goodness, topped with bell peppers and onion and fries", 7.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/Italian_mogyfk.jpg', 3))
        menu_list.append(Menu_Item(
            1, "Sonora", "Bacon wrapped and topped with relish, tomoatoes, avacados, and onions", 8.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/Sonora_ixb68i.jpg', 5))
        menu_list.append(Menu_Item(
            1, "Kansas City", "Kansas City style hot dog, all beef and topped with saurkraut and swiss cheese", 8.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/Kansas_City_zqcydk.jpg', 4))
        menu_list.append(Menu_Item(2, "French Fries",
                         "Our world famous fries", 3.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/fries_zupc26.jpg', 2))
        menu_list.append(Menu_Item(2, "Onion Rings",
                         "Breaded onion circles", 4.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/onion_rings_am1rph.jpg', 1))
        menu_list.append(
            Menu_Item(2, "Chips", "Fresh baked potato chips", 3.50, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616299/HotDogFT/chips_roidrb.jpg',3))
        menu_list.append(Menu_Item(3, "Chocolate Chip Cookie",
                                   "Eat this cookie for world peace", 2.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/cookie_vqicvs.jpg', 2))

        menu_list.append(
            Menu_Item(3, "Pickle", "This pickle is the real dill", 1.50, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/pickle_ay2o7n.jpg', 1))

        menu_list.append(Menu_Item(4, "20oz Coca-Cola",
                                   "The perfect way to wash down a hot dog", 1.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/coca_cola_axoxem.jpg', 1))
        menu_list.append(
            Menu_Item(4, "Iced Tea", "A Southern Classic", 1.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616298/HotDogFT/tea_iawvzt.jpg', 2))
        menu_list.append(Menu_Item(
            4, "Lemonade", "Freshly Squeezed to help you beat the heat while you eat our meat", 1.99, 'https://res.cloudinary.com/coding-temple/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1623616299/HotDogFT/lemonade_j94ahq.jpg', 23))

        for item in menu_list:
            db.session.add(item)
        db.session.commit()

    @staticmethod
    def db_init_menu_ingredients():
        meal_ingredients = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 10), (3, 3), (3, 9), (3, 11), (3, 15),
                            (4, 1), (4, 3), (4, 7), (4, 8), (4, 12), (4, 13), (5, 14), (5, 16)]
        for ingredient in meal_ingredients:
            add = Meal_Ingredient(ingredient[0], ingredient[1])
        db.session.commit()

    @staticmethod
    def db_init_payment_type():
        pay_types = ["Cash", "Credit", "Stripe"]
        for pay_type in pay_types:
            add = Payment_Type(pay_type)
            db.session.add(add)
        db.session.commit()

    @staticmethod
    def db_init_order_status():
        statii = ["Cooking, Complete, Pending"]
        for status in statii:
            add = Order_Status(status)
            db.session.add(add)
        db.session.commit()


class Db_Destroy():

    @staticmethod
    def db_destroy():
        db.reflect()
        db.drop_all()
