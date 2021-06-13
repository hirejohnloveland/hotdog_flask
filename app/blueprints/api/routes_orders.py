from flask import request, jsonify, abort
from . import bp as api
from app import db
from app.blueprints.users.models import User_Anonymous
from app.blueprints.orders.models import Order, Order_Item, Order_Item_Ingredient
from app.blueprints.menu.models import Ingredient, Menu_Item

#######################################################
######## Get the Cart #################################
#######################################################


@api.route('/order/cart', methods=['GET'])
def view_cart():
    """
    [GET] /api/order/cart
    """

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(acquire_token(request))
    if not user:
        return abort(401)

    order = Order.get_order(user)
    results = db.session.query(Menu_Item.category_id, Menu_Item.display_order,
                               Menu_Item.name, Menu_Item.price, Order_Item.id).join(Order_Item).filter_by(order_id=order.id)

    def query_to_dict(record):
        return {
            'cart_item_category': record[0],
            'cart_item_display': record[1],
            'cart-item_name': record[2],
            'cart_item_price': record[3],
            'order_item_id': record[4]
        }

    return jsonify([query_to_dict(result) for result in results])

#######################################################
######## Get the Ingredients ##########################
#######################################################


@api.route('/order/ingredients/<int:order_item_id>', methods=['GET'])
def get_item_ingredients(order_item_id):

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(token := acquire_token(request))
    if not user:
        return abort(401)

    # Authenticate order belongs to user - or send back 403
    if not Order.is_authentic(order_item_id, token):
        return abort(403)

    results = db.session.query(Ingredient.name, Order_Item_Ingredient.ingredient_amount).join(
        Order_Item_Ingredient).filter_by(order_item_id=order_item_id)

    def query_to_dict(record):
        return {
            'ingredient_name': record[0],
            'ingredient_amount': record[1]
        }

    return jsonify([query_to_dict(result) for result in results])

#######################################################
######## Add an Item to the Cart ######################
#######################################################


@api.route('/order/add/<int:menu_item>', methods=['POST'])
def add_item(menu_item):
    """
    [POST] /api/order/add/<int:menu_item>
    """

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(acquire_token(request))
    if not user:
        return abort(401)

    order = Order.get_order(user)
    Order_Item(menu_item, order.id)
    return success200()

#######################################################
######## Remove an Item from the Cart #################
#######################################################


@api.route('/order/remove/<int:order_item_id>', methods=['POST'])
def remove_order(order_item_id):
    """
    [POST] /api/order/remove/<int:order_item_id>
    """

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(token := acquire_token(request))
    if not user:
        return abort(401)

    # Authenticate order belongs to user - or send back 403
    if not Order.is_authentic(order_item_id, token):
        return abort(403)

    Order_Item.delete(order_item_id)
    return success200()

#######################################################
######## Change the Ingredients  ######################
#######################################################


@api.route('/order/ingredient/<int:order_item>/<int:order_ingredient_id>/<int:amount>', methods=['POST'])
def udpate_ingredient(order_item, order_ingredient_id, amount):
    """
    [POST] /api/order/ingredient/<int:order_item>/<int:order_ingredient_id>/<int:amount>
    """

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(token := acquire_token(request))
    if not user:
        return abort(401)

    # Authenticate order belongs to user - or send back 403
    if not Order.is_authentic(order_item, token):
        return abort(403)

    # Only accept valid input- or reject with 403
    if not (amount == 0 or amount == 1 or amount == 2):
        return abort(403)

    Order_Item_Ingredient.update(order_ingredient_id, amount)
    return success200()

#######################################################
######## Delete the Cart  #############################
#######################################################


@api.route('/order/delete', methods=['POST'])
def delete_order():
    """
    [GET] /api/categories
    """

    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(token := acquire_token(request))
    if not user:
        return abort(401)

    Order.delete_pending_order(token)
    return success200()

#######################################################
######## Checkout  ####################################
#######################################################
# TODO #### Integrate Stripe Pay into this route and
# authenticate payment has occured.


@api.route('/order/checkout', methods=['POST'])
def checkout():
    """
    [GET] /api/categories
    """
    # Authenticate user - or send back 401 to trigger new token
    user = User_Anonymous.check_token(token := acquire_token(request))
    if not user:
        # Return 401 to client.  Client then requests a new token
        return abort(401)

    Order.complete_checkout(token)
    return success200()

#######################################################
######## Helper Functions #############################
#######################################################


def acquire_token(request):
    auth_header = request.headers.get('Authorization')
    token = str.split(auth_header)[1]
    return token


def success200():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp
