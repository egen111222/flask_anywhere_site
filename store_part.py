from flask import Blueprint, render_template,session
from store_models import Item,Order
from cart import Cart


store_app = Blueprint('store_app', __name__,
                        template_folder='templates')


@store_app.route("/")
def view_items():
    items = Item.query.all()
    return render_template("store/items.html",
                           items=items)

@store_app.route("/<int:item_number>")
def view_item(item_number):
    item = Item.query\
           .filter(Item.id==item_number)\
           .first()
    return render_template("store/item.html",
                           item=item)


@store_app.route("/add__to_cart/<int:item_number>")
def add_to_cart(item_number):
    item = Item.query.filter(Item.id==item_number).first()
    if item:
        if session.get("cart"):
            session["cart"].add_item(item)
        else:
            session["cart"] = Cart()
            session["cart"].add_item(item)
        return f"Товар {item} додано"
    return "Виникла помилка неіснуючий товар"


@store_app.route("/cart")
def view_cart():
    return render_template("store/cart.html")

