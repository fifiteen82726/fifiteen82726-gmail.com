from flask import Flask, escape, request, render_template
from form import RegistrationForm, LoginForm

app = Flask(__name__)
# TODO, env file
app.config['SECRET_KEY'] = 'bfa07090f91443d084e0b09e9e359e22'

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
def hello():
    name = request.args.get("name", "2212")
    return f'Hello, {escape(name)}!'

@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Title')

@app.route('/register')
def register():
    form = RegistrationForm()
    print(form)
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__  == '__main__':
    app.run()

