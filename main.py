from flask import Flask, render_template
import requests


response = requests.get('https://api.npoint.io/4964104e0ae06aa7ec8b')
all_blogs = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_blogs)


@app.route('/post/<int:num>')
def my_posts(num):
    current_blog = None
    print(num)
    for blog in all_blogs:
        if blog['id'] == num:
            current_blog = blog
    return render_template('post.html', post=current_blog)


if __name__ == "__main__":
    app.run(debug=True)
