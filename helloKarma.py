from flask import Flask

app = Flask(__name__)

@app.route("/karma")
def hello_karma():
    return "<h1> Hello Karma!</h1>"