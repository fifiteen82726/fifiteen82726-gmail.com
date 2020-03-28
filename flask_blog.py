from flask import Flask, escape, request, render_template, flash, redirect, url_for
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

