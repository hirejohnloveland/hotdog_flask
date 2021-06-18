from flask import request, jsonify
from . import bp as api
from app.blueprints.menu.models import Category, Menu_Item, Meal_Ingredient, Ingredient
from app import db


########################################################
######### Get Categories ###############################
########################################################

@api.route('/categories')
def get_categories():
    """
    [GET] /api/categories
    """
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

########################################################
######### Get Menu Items  ##############################
########################################################


@api.route('/menuitems/<int:cat_id>')
def get_items(cat_id):
    """
    [GET] /api/menuitems/<int:cat_id>
    """
    items = Menu_Item.query.filter_by(category_id = cat_id).all()
    return jsonify([item.to_dict() for item in items])

########################################################
######### Get Ingredients  #############################
########################################################


@api.route('/ingredients/<int:meal_id>')
def get_ingredients(meal_id):
    """
    [GET] /api/ingredients
    """

    
    ingredients = db.session.query(Ingredient.id, Ingredient.name).join(Meal_Ingredient).filter_by(menu_item_id=meal_id)
 
    def query_to_dict(record):
        return {
            'ingredient_id': record[0],
            'ingredient_name': record[1]

        }

    return jsonify([query_to_dict(ingredient) for ingredient in ingredients])
    
