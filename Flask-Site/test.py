from flask import Flask , url_for ,redirect,request
app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return "<h1>This is a Profile page for %s </h1>"%username

app.route('/profile/<id>')
def profile(id):
    return "<h1>This is a Profile page for %d </h1>"%id

@app.route('/admin')
def welcome_admin():
    return "Welcome Admin"

@app.route('/guest/<guest>')
def welcome_guest(guest):
    return " Welcom guest %s"%guest

@app.route('/user/<name>')
def welcome_user(name):
    if name =="admin":
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for('welcome_guest',guest=name))
app.run(debug=True)