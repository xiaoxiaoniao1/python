from flask import Flask, render_template, request

app = Flask(__name__)

class Product:
    pass

@app.route("/post/<name>")
def post(name):
    return render_template("post.html", name=name)

@app.route("/product")
def product():
    #1
    #id = request.args["id"]
    #author = request.args["author"]
    #return render_template("product.html", id=id, author=author)

    #2
    #return render_template("product.html", data=request.args)

    #3
    product = Product()
    product.id = request.args["id"]
    product.author = request.args["author"]
    return render_template("product.html", data=product)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
