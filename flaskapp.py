from flask import Flask, escape, request, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Luis Ariel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Aaron Luis',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2020'
    },
    {
        'author': 'Lis Serrano',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'April 3, 2020'
    },
    {
        'author': 'Chabelys Pérez',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'March 10, 2020'
    },
]

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "Home")
    return render_template('./home_view/home.html', title = 'Home', posts = posts)

@app.route('/about')
def about():
    name = request.args.get("name", "About")
    return render_template('./about_view/about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)