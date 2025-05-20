from flask import Flask

app = Flask(__name__)

@app.route("/kitty")
def hello_karma():
    return "<h1> Hello Kitty!</h1>"