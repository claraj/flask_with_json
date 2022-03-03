from flask import Flask, render_template, request 

app = Flask(__name__)





@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/place')
def place_facts():
    city = request.args.get('place')

    dictionary_of_stuff = {   # some random data 
        'numbers': [1, 2, 3],
        'businesses': ['coffee', 'pizza', 'gyms'],
        'videos': 'some video info here',
        'message': 'hello'
    }

    return render_template('place.html', stuff=dictionary_of_stuff)