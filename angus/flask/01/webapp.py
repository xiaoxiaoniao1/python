from flask import Flask
import json

app = Flask(__name__)

count = 0

# MVC Model(Class Product) view Controller

# class Product:
#     id
#     url
#     price

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home")
def home():
    names  = ["angus", "leif"]
    name_idx = count % 2
    name = names[name_idx]

    global count
    count+=1

    html = ""
    with open("./home.html", "r") as f:
        html = f.read()

    return html.replace("{name}", name)

@app.route("/book")
def book():
    html = ""
    with open("./book.html", "r") as f:
        html = f.read()
    return html

@app.route("/books")
def book_data():
    names  = ["python", "java"]
    name_idx = count % 2
    name = names[name_idx]

    global count
    count+=1

    return json.dumps({"name": name})

# @app.route("/*")
# def static():
#     content = ""
#     with open(".", "r") as f:
#         content = f.read()
#     return content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
