from flask import request, jsonify
from . import bp as api
from app.blueprints.menu.models import Category, Menu_Item, Meal_Ingredient, Ingredient
from app import db


########################################################
######### Get Categories ###############################
########################################################

@api.route('/categories', methods=['GET'])
def get_categories():
    """
    [GET] /api/categories
    """
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

########################################################
######### Get Menu Item  ###############################
########################################################


@api.route('/menuitems', methods=['GET'])
def get_items():
    """
    [GET] /api/menuitems
    """
    items = Menu_Item.query.all()
    return jsonify([item.to_dict() for item in items])

########################################################
######### Get Ingredients  #############################
########################################################


@api.route('/ingredients/<int:meal_id>', methods=['POST'])
def get_ingredients(meal_id):
    """
    [POST] /api/ingredients
    """

    
    ingredients = db.session.query(Ingredient.id, Ingredient.name).join(Meal_Ingredient).filter_by(menu_item_id=meal_id)
 
    def query_to_dict(record):
        return {
            'ingredient_id': record[0],
            'ingredient_name': record[1]

        }

    return jsonify([query_to_dict(ingredient) for ingredient in ingredients])
    
