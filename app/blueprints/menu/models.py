from app import db


class Category(db.Model):
    # Manages the different types of products
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
    # Manages the menu
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)  # FKey
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String(250))
    display_order = db.Column(db.Integer, nullable=False)
    menu_item = db.relationship(
        'Meal_Ingredient', backref='menu_item', lazy='dynamic')
    order_item = db.relationship(
        'Order_Item', backref='Menu_Item', lazy='dynamic')

    def __init__(self, category_id, name, desc, price, img_url, display_order):
        self.category_id = category_id
        self.name = name
        self.desc = desc
        self.price = price
        self.img_url = img_url
        self.display_order = display_order

    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'desc': self.desc,
            'price': self.price,
            'image': self.img_url,
            'display_order': self.display_order
        }


class Meal_Ingredient(db.Model):
    # Many to many table associating individual menu items with individual ingredients
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
    # Manage the ingredients
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.relationship(
        'Meal_Ingredient', backref='ingredient', lazy='dynamic')
    order__item__ingredient = db.relationship(
        'Order_Item_Ingredient', backref='Ingredient', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
