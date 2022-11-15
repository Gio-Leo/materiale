# import module
from flask import Flask, render_template

# create the application
app = Flask(__name__)

# define the homepage
@app.route('/')
def index():
    pPosts = [
        {'id': 1234, 'usrname': '@luigi', 'usrimg': 'derussis.jpg', 'img': 'img1.jpg',
         'date': '1 giorno fa', 'post': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula. Ut ultrices a nibh eget eleifend. Nullam eleifend metus nec erat vestibulum venenatis ornare sed orci. Donec vel sapien sit amet felis cursus rutrum.'},
        {'id': 5678, 'usrname': '@alberto', 'usrimg': 'monge.jpg', 'img': 'img2.jpg',
         'date': '4 giorni fa', 'post': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula. Ut ultrices a nibh eget eleifend. Nullam eleifend metus nec erat vestibulum venenatis ornare sed orci. Donec vel sapien sit amet felis cursus rutrum.'},
        {'id': 9012, 'usrname': '@juan', 'usrimg': 'saenz.png', 'img': 'img3.jpg',
         'date': '2 settimane fa', 'post': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie. Donec laoreet iaculis nibh sed viverra. Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at. Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula. Ut ultrices a nibh eget eleifend. Nullam eleifend metus nec erat vestibulum venenatis ornare sed orci. Donec vel sapien sit amet felis cursus rutrum.'}
    ]
    return render_template('index.html', posts=pPosts)

# define the 'about' page
@app.route('/about')
def about():
    pDevelopers = [
        {'id': 1234, 'name': 'Luigi De Russis', 'devimg': 'derussis.jpg',
            'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'First quote author'},
        {'id': 5678, 'name': 'Alberto Monge Roffarello', 'devimg': 'monge.jpg',
            'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Second quote author'},
        {'id': 9012, 'name': 'Juan Pablo Sáenz', 'devimg': 'saenz.png',
            'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Third quote author'}
    ]
    return render_template('about.html', developers=pDevelopers)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)