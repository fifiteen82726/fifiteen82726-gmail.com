from flask import Flask, escape, request, render_template, flash, redirect, url_for
from form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# TODO, env file
app.config['SECRET_KEY'] = 'bfa07090f91443d084e0b09e9e359e22'
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_NAME = 'flask_blog'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}'
db = SQLAlchemy(app)


# from flask_blog import db
# db.create_all()
# create user and post
# user = User(username='coda0726', email: 'hjikjnjhnj@njkjkjjk.com', password=''bjokjkoj)
# db.session.add(user)
# db.session.commit()
# post_1 = Post(title='Blog1', content='content', user_id=user.id)
# db.session.add(post_1)
# db.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # create user relationship, not column
    # use uppercase
    posts = db.relationship('Post', backref='author', lazy=True)

    # how this object is printing out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # use lowercase
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': '4/20/2018',
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': '4/20/2018',
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts, title='Title')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # print(form.validate_on_submit())
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == 'fifiteen82726@gmail.com' and form.password.data == '123123123':
        return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

if __name__  == '__main__':
    app.run()

