from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/')
def homepage():
    ##image_names = os.listdir('./images')
    ##return render_template("index.html", image_names=image_names)
    return render_template("index.html")

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/recipe.html')
def recipe():
    return render_template("recipe.html")

@app.route('/recipe_generator.html', methods=['GET', 'POST'])
def recipe_generator():
    return render_template("recipe_generator.html")
##def recipe_generator():
    ##    if request.method == 'POST':
    ##        a =  request.form[]
    ##        b =  request.form['vegtables']
    ##        selectedValue = a+b
    ##        return redirect(url_for('click', selectedValue=selectedValue))


## @app.route('/<selectedValue>')
## def click('meal_type'):
    ## return render_template(nocarbs.html)

@app.route('/detox.html')
def detox():
    return render_template("detox.html")

@app.route('/gallery.html')
def gallery():
    return render_template("gallery.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/nocarbs.html')
def nocarbs():
    return render_template("nocarbs.html")


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "Email sent"

##def toggle_display():
##    el = document.querySelector('.content_section');
##    if el.style.visibility == 'hidden':
##        el.style.visibility = 'visible'
##    else: el.style.visibility = 'hidden'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
