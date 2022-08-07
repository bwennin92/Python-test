from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return {"home":"id"}



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


app.run('localhost', 8080, True)
