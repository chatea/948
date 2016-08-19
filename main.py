from flask import Flask
import menu

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello 948, Just Buy!"

if __name__ == "__main__":
    app.run()
