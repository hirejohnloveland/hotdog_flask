from app import db
from datetime import datetime
from app.blueprints.menu.models import *


class Payment_Type(db.Model):
    # Manages different payment types
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order = db.relationship('Order', backref='payment', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Order_Status(db.Model):
    # Manages different order stati
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order = db.relationship('Order', backref='status', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Order(db.Model):
    # Manages individual carts (orders)
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    originator = db.Column(db.String(50), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey(
        Order_Status.id), nullable=False)
    paymenent_type_id = db.Column(
        db.Integer, db.ForeignKey(Payment_Type.id), nullable=False)
    order_items = db.relationship(
        'Order_Item', backref='Order', lazy='dynamic')

    def __init__(self, status_id, paymenent_type_id, originator):
        self.status_id = status_id
        self.originator = originator
        self.paymenent_type_id = paymenent_type_id

    def is_authentic(order_item_id, token):
        order_token = db.session.query(Order.originator).join(
            Order_Item).filter_by(id=order_item_id).first()
        if not(order_token):
            return
        return (order_token[0] == token)

    @staticmethod
    def get_order(user):
        order = Order.query.filter_by(
            originator=user.token, status_id=3).first()
        if order:
            return order
        else:
            order = Order(3, 3, user.token)
            db.session.add(order)
            db.session.commit()
            return order

    @staticmethod
    def complete_checkout(token):
        order = Order.query.filter_by(
            originator=token, status_id=3).first()
        if not order:
            return
        order.status_id = 1
        db.session.commit()

    @staticmethod
    def delete_pending_order(token):
        order = Order.query.filter_by(
            originator=token, status_id=3).first()
        if not order:
            return
        order_items = Order_Item.query.filter_by(order_id=order.id).all()
        for order_item in order_items:
            Order_Item.delete(order_item.id)


class Order_Item(db.Model):
    # Manages the many to many relationship between menu items and orders
    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey(
        Menu_Item.id), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(Order.id), nullable=False)
    order_item_ingredient = db.relationship(
        'Order_Item_Ingredient', backref='order_item', lazy='dynamic')

    def __init__(self, menu_item_id, order_id):
        self.menu_item_id = menu_item_id
        self.order_id = order_id
        db.session.add(self)
        db.session.commit()
        Order_Item_Ingredient.add(menu_item_id, self.id)

    @staticmethod
    def delete(order_item_id):
        Order_Item_Ingredient.delete(order_item_id)
        order_item = Order_Item.query.filter_by(id=order_item_id).first()
        if not order_item:
            return
        db.session.delete(order_item)
        db.session.commit()


class Order_Item_Ingredient(db.Model):
    # Manages the unique ingredients of each item on an order
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(
        db.Integer, db.ForeignKey(Ingredient.id), nullable=False)
    order_item_id = db.Column(
        db.Integer, db.ForeignKey(Order_Item.id), nullable=False)
    ingredient_amount = db.Column(db.Integer, nullable=False)

    def __init__(self, ingredient_id, order_item_id, ingredient_amount):
        self.ingredient_id = ingredient_id
        self.order_item_id = order_item_id
        self.ingredient_amount = ingredient_amount
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def add(menu_item_id, order_item_id):
        ingredients = db.session.query(Ingredient.id).join(
            Meal_Ingredient).filter_by(menu_item_id=menu_item_id)
        for ingredient in ingredients:
            Order_Item_Ingredient(ingredient[0], order_item_id, 1)

    @staticmethod
    def delete(order_item_id):
        ingredients = Order_Item_Ingredient.query.filter_by(
            order_item_id=order_item_id).all()
        if not ingredients:
            return
        for ingredient in ingredients:
            db.session.delete(ingredient)
        db.session.commit()

    @staticmethod
    def update(order_ingredient_id, amount):
        ingredient = Order_Item_Ingredient.query.filter_by(
            id=order_ingredient_id).first()
        ingredient.ingredient_amount = amount
        db.session.commit()
