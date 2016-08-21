from flask import Flask
from flask import request
import json
import menu
import optimizer

app = Flask(__name__)
app.debug = True

MENU_NAME_ID_MAP = {
    u'test': u'-1',
    u'mcdonalds': u'0',
}

@app.route("/")
def home():
    return "Hello 948, Just Buy!"


@app.route("/menus")
def menus():
    menulist = menu.get_menu_list()
    menus = []
    for k, v in menulist.items():
        menus.append(v)
    return json.dumps(menus)


@app.route("/menus/<path:menu_name>")
def get_menu(menu_name):
    if menu_name not in MENU_NAME_ID_MAP:
        return "{}"

    menu_id = MENU_NAME_ID_MAP[menu_name]
    target_menu = menu.get_menu(menu_id)
    menu_items = []
    for k, v in target_menu.items():
        menu_items.append(v)
    return json.dumps(menu_items)


@app.route("/getPrices",  methods=['GET'])
def get_prices():
    menu_id = request.args.get(u'menu_id')
    orders = json.loads(request.args.get(u'orders'))
    orders = [unicode(str(order), "utf-8") for order in orders]
    print menu_id, orders
    order_method = optimizer.get_best_order_way(menu_id, orders)
    result = {
        u"items":order_method.items,
        u"prices":order_method.prices
    }
    return json.dumps(result)


@app.errorhandler(404)
def page_not_found(e):
    return "404: Sorry, there is not such page!"


@app.errorhandler(500)
def page_not_found(e):
    return "500: Sorry, some bug happend!!!"


if app.debug:
    @app.route("/test")
    def test():
        target_menu = menu.get_menu(u'-1')
        menus = []
        for k, v in target_menu.items():
            menus.append(v)
        return json.dumps(menus)
