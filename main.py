from flask import Flask, render_template,request,jsonify
import requests
import datetime
import smtplib
import os
year=datetime.datetime.now().year



posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts,year=year)


@app.route("/about")
def about():
    return render_template("about.html",year=year)


@app.route("/contact",methods=["GET","POST"])
def contact():
    my_mail="harshpandey1789@gmail.com"
    password="jgohssrnajotodiy"
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_mail,password=password)
                connection.sendmail(from_addr=my_mail,to_addrs=my_mail,msg=f"Subject:Contact Me\n\n{name,phone,message}")
                connection.close()

        return render_template("contact.html",name=name,email=email,phone=phone,message=message,msg_sent=True)
    else:
        return render_template("contact.html",year=year,msg_sent=False)




@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,year=year)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
