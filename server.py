from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", name="")

@app.route("/<name>")
def hellomoto(name):
    import ipdb; ipdb.set_trace()
    print("path=%s" % (request.path))
    return render_template("demo.html", name=name)

@app.route("/user/<int:userid>")
def new(userid):
    return "User id: %s" % userid

@app.route("/post/<int:postid>", methods=["GET"])
def get_post(postid):
    return "Getting post id: %s" % postid

@app.route("/posts/<int:postid>", methods=["DELETE"])
def delete_post(postid):
    return "Deleting post id: %s" % postid


@app.route("/posts/<int:postid>", methods=["PUT"])
def update_post(postid):
    return "Updating post id: %s" % postid


@app.route("/posts/<int:postid>", methods=["PATCH"])
def update_single_field_post(postid):
    return "Patching post id: %s" % postid


