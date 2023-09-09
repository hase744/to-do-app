from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
@application.route("/index")
def index():
    # Note:str()を使う事でNoneの時でも、TypeErrorを起こさず"様"をつけることが出来る
    name  = str(request.args.get("name")) + "様"
    return render_template("index.html", name=name)

@application.route("/adv", methods=["GET", "POST"])
def advance():
    # Note:dictのgetメソッドを使うことでNoneでもエラーにならない！
    name  = request.form.get("name")
    # Note:./を書いても書かなくてもいいんだなぁ。
    return render_template("./advance.html", name=name)


if __name__ == "__main__":
    application.run()