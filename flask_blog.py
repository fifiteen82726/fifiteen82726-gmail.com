from flask import Flask, escape, request, render_template

app = Flask(__name__)

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
    return render_template('home.html', posts=posts)

if __name__  == '__main__':
    app.run()

