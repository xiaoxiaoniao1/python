from flask import Flask, request

app = Flask(__name__)

@app.route("/product", methods=['GET', 'POST'])
def product():
    id = request.form["id"]
    author = request.form["author"]
    return "id=%s, author=%s" % (id, author)

#/artcle?id=xxx
@app.route("/artcle")
def artcle():
    id = request.args["id"]
    author = request.args["author"]
    print request.content_type, request.content_length, request.base_url, request.path,  request.values, request.query_string
    return "id=%s, author=%s" % (id, author)

@app.route("/<name>")
def index(name):
    content = b""
    with open(name, "r") as f:
        content = f.read()
    return content


@app.route("/post/<post_id>")
def post(post_id):
    return post_id


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
