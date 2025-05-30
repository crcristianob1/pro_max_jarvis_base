from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Pro Max JARVIS Turbo está online!</h1>"
