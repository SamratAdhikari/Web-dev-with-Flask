'''       SamaShare Share App
Author  : Global Gang
Date    : 28 June 2021
Purpose : Commercial Purpose
'''


# ---------------Modules-----------------------------
from flask import Flask, render_template

# -----------------Custom Modules--------------------
from fields import *


# ----------------Initialize flask app--------------
app = Flask(__name__)
app.secret_key = 'samrat'


# ---------------------Configure database----------------
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres://whwowhdqlwmktq:7a015915b262dab14d4fc890ec4bc02f96de8cca7bab756a7ffac3d8316e9fa8@ec2-34-233-114-40.compute-1.amazonaws.com:5432/ddesjap714q857'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# ----------------For User Login Authentication---------------

# -------------------Routes----------------
# Route for index/home page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Route for register page
@app.route('/register')
def register():
    reg_form = RegistrationForm()
    # return 'Great Success'
    if reg_form.validate_on_submit():
        return 'Great Success'

    return render_template('register.html', form=reg_form)


# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')


# Route for news page
@app.route('/news')
def news():
    return render_template('news.html')


# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# --------------------------Run the program------------------------
if __name__ == '__main__':
    app.run(debug=True)
