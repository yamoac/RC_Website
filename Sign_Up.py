import requests
def send_simple_message():
    return requests.post(
    "https://api.mailgun.net/v3/sandboxf1b7a46a2d934c1097903b166b690197.mailgun.org/messages",
        auth=("api", "6e1de8eb5242fab6b6721631d3fd81a7-7caa9475-44e4fc0c"),
        data={"from": "Excited User <mailgun@sandboxf1b7a46a2d934c1097903b166b690197.mailgun.org>",
            "to": ["rorleanslindsay@gmail.com"],
            "subject": "Welcome!!",
            "text": "Welcome to Recipe Room! Get ready to create some awesome, healthy recipes"})
send_simple_message()


from flask import Flask, render_template, request
app = Flask ("MyApp")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def homepage():
    return render_template("index.html")

@app.route("/recipe.html")
def recipe():
    return render_template("recipe.html")

@app.route("/detox.html")
def detox():
    return render_template("detox.html")

@app.route("/gallery.html")
def gallery():
        return render_template("gallery.html")

@app.route("/Form.html")
def signup():
    return render_template("Form.html")

@app.route("/nocarbs.html")
def nocarbs():
    return render_template("nocarbs.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "Yay! You're all signed up. We look forward to sharing some delicious recipes with you!"

app.run(debug=True)
