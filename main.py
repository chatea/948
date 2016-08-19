from flask import Flask
import json
import menu

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return "Hello 948, Just Buy!"


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
        return json.dumps(target_menu)
