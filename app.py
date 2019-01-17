from flask import Flask
app = Flask(__name__)
WORD= "Hello, World!"

@app.route("/users", methods=["GET"])
def home():
    with open("word.txt") as f:
        return f.readline()

@app.route("/users", methods=["POST"])
def add():
    with open("word.txt", "w+") as f:
        f.write("Holy poop, it wrote")
    return '200'
