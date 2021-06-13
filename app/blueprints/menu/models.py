from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    display_order = db.Column(db.Integer, nullable=False)
    items = db.relationship('Menu_Item', backref='Category', lazy='dynamic')

    def __init__(self, name, display_order):
        self.name = name
        self.display_order = display_order

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'display_order': self.display_order
        }


class Menu_Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)  # FKey
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    display_order = db.Column(db.Integer, nullable=False)
    menu_item = db.relationship(
        'Meal_Ingredient', backref='menu_item', lazy='dynamic')
    order_item = db.relationship(
        'Order_Item', backref='Menu_Item', lazy='dynamic')

    def __init__(self, category_id, name, desc, price, display_order):
        self.category_id = category_id
        self.name = name
        self.desc = desc
        self.price = price
        self.display_order = display_order

    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'desc': self.desc,
            'price': self.price,
            'display_order': self.display_order
        }


class Meal_Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey(
        Menu_Item.id), nullable=False)  # Fkey
    ingredient_id = db.Column(db.Integer, db.ForeignKey(
        'ingredient.id'), nullable=False)

    def __init__(self, menu_item_id, ingredient_id):
        self.menu_item_id = menu_item_id
        self.ingredient_id = ingredient_id

    def to_dict(self):
        return {
            'id': self.id,
            'menu_item': self.menu_item_id,
            'ingredient_item': self.ingredient_id
        }


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.relationship(
        'Meal_Ingredient', backref='ingredient', lazy='dynamic')
    order__item__ingredient = db.relationship('Order_Item_Ingredient', backref='Ingredient', lazy='dynamic')
    

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


###############################################
####### Initialization Script #################
###############################################

def db_init():
    cat1 = Category("Dogs", 1)  # id = 1
    db.session.add(cat1)
    cat2 = Category("Sides", 2)  # id = 2
    db.session.add(cat2)
    cat3 = Category("Extras", 3)  # id = 3
    db.session.add(cat3)
    cat4 = Category("Beverages", 4)  # id = 4
    db.session.add(cat4)

    ing1 = Ingredient("Bacon")
    db.session.add(ing1)
    ing2 = Ingredient("Grilled Peppers")
    db.session.add(ing2)
    ing3 = Ingredient("Onion")
    db.session.add(ing3)
    ing4 = Ingredient("Jalepenos")
    db.session.add(ing4)
    ing5 = Ingredient("Pickle Spear")
    db.session.add(ing5)
    ing6 = Ingredient("Celery Salt")
    db.session.add(ing6)
    ing7 = Ingredient("Green Relish")
    db.session.add(ing7)
    ing8 = Ingredient("Tomatoes")
    db.session.add(ing8)
    ing9 = Ingredient("Mustard")
    db.session.add(ing9)
    ing10 = Ingredient("Bell Peppers")
    db.session.add(ing10)
    ing11 = Ingredient("Ketchup")
    db.session.add(ing11)
    ing12 = Ingredient("Avacado Chunks")
    db.session.add(ing12)
    ing13 = Ingredient("Mayonnaise")
    db.session.add(ing13)
    ing14 = Ingredient("Saurkraut")
    db.session.add(ing14)
    ing15 = Ingredient("French Fries")
    db.session.add(ing15)
    ing16 = Ingredient("Swiss Cheese")
    db.session.add(ing16)

    dog1 = Menu_Item(
        1, "Tijuana", "Bacon wrapped all beef hot dog with grille peppers and jalepenos", 8.99, 2)
    d1mi1 = Meal_Ingredient(1, 1)
    d1mi2 = Meal_Ingredient(1, 2)
    d1mi3 = Meal_Ingredient(1, 3)
    d1mi4 = Meal_Ingredient(1, 4)
    db.session.add(dog1)
    db.session.add(d1mi1)
    db.session.add(d1mi2)
    db.session.add(d1mi3)
    db.session.add(d1mi4)

    dog2 = Menu_Item(
        1, "Chicago", "All Beef hot dog topped with onions, tomatoes, relish, and a pickle spear on a poppy seed bun", 7.99, 1)
    d2mi1 = Meal_Ingredient(2, 3)
    d2mi2 = Meal_Ingredient(2, 5)
    d2mi3 = Meal_Ingredient(2, 6)
    d2mi4 = Meal_Ingredient(2, 7)
    d2mi5 = Meal_Ingredient(2, 8)
    d2mi6 = Meal_Ingredient(2, 9)
    db.session.add(dog2)
    db.session.add(d2mi1)
    db.session.add(d2mi2)
    db.session.add(d2mi3)
    db.session.add(d2mi4)
    db.session.add(d2mi5)
    db.session.add(d2mi6)

    dog3 = Menu_Item(
        1, "Italian", "Deep friend doggy goodness, topped with bell peppers and onion and fries", 7.99, 3)
    d3mi1 = Meal_Ingredient(3, 10)
    d3mi2 = Meal_Ingredient(3, 3)
    d3mi3 = Meal_Ingredient(3, 9)
    d3mi4 = Meal_Ingredient(3, 11)
    d3mi5 = Meal_Ingredient(3, 15)
    db.session.add(dog3)
    db.session.add(d3mi1)
    db.session.add(d3mi2)
    db.session.add(d3mi3)
    db.session.add(d3mi4)
    db.session.add(d3mi5)

    dog4 = Menu_Item(
        1, "Sonora", "Bacon wrapped and topped with relish, tomoatoes, avacados, and onions", 8.99, 5)
    d4mi1 = Meal_Ingredient(4, 1)
    d4mi2 = Meal_Ingredient(4, 3)
    d4mi3 = Meal_Ingredient(4, 7)
    d4mi4 = Meal_Ingredient(4, 8)
    d4mi5 = Meal_Ingredient(4, 12)
    d4mi6 = Meal_Ingredient(4, 13)
    db.session.add(dog4)
    db.session.add(d4mi1)
    db.session.add(d4mi2)
    db.session.add(d4mi3)
    db.session.add(d4mi4)
    db.session.add(d4mi5)
    db.session.add(d4mi6)

    dog5 = Menu_Item(
        1, "Kansas City", "Kansas City style hot dog, all beef and topped with saurkraut and swiss cheese", 8.99, 4)
    d5mi1 = Meal_Ingredient(5, 14)
    d5mi2 = Meal_Ingredient(5, 16)
    db.session.add(dog5)
    db.session.add(d5mi1)
    db.session.add(d5mi2)

    sides1 = Menu_Item(2, "French Fries", "Our world famous fries", 3.99,  2)
    sides2 = Menu_Item(2, "Onion Rings", "Breaded onion circles", 4.99, 1)
    sides3 = Menu_Item(2, "Chips", "Fresh baked potato chips", 3.50, 3)
    extras1 = Menu_Item(3, "Chocolate Chip Cookie",
                        "Eat this cookie for world peace", 2.99, 2)
    extras2 = Menu_Item(3, "Pickle", "This pickle is the real dill", 1.50, 1)
    bev1 = Menu_Item(4, "20oz Coca-Cola",
                     "The perfect way to wash down a hot dog", 1.99, 1)
    bev2 = Menu_Item(4, "Iced Tea", "A Southern Classic", 1.99, 2)
    bev3 = Menu_Item(
        3, "Lemonade", "Freshly Squeezed to help you beat the heat while you eat our meat", 1.99, 3)
    db.session.add(sides1)
    db.session.add(sides2)
    db.session.add(sides3)
    db.session.add(extras1)
    db.session.add(extras2)
    db.session.add(bev1)
    db.session.add(bev2)
    db.session.add(bev3)
    db.session.commit()
