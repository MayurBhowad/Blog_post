from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return '<h1>contact Page!</h1>'


if __name__ == '__main__':
    app.run(debug=True)

