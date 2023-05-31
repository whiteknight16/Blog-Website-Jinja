from flask import Flask, render_template
import requests
import datetime

year=datetime.datetime.now().year



posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts,year=year)


@app.route("/about")
def about():
    return render_template("about.html",year=year)


@app.route("/contact")
def contact():
    return render_template("contact.html",year=year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,year=year)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
