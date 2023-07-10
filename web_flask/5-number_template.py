#!/usr/bin/python3
'''
A simple Flask web application.
'''
from flask import Flask, render_template


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''
    Renders the home page.

    Returns:
        str: The greeting message.
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    Renders the hbnb page.

    Returns:
        str: The HBNB message.
    '''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''
    Renders the c page.

    Args:
        text (str): The text parameter from the URL.

    Returns:
        str: The formatted C message.
    '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''
    Renders the python page.

    Args:
        text (str): The text parameter from the URL.

    Returns:
        str: The formatted Python message.
    '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''
    Renders the number page.

    Args:
        n (int): The number parameter from the URL.

    Returns:
        str: The formatted number message.
    '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    Renders the number_template page.

    Args:
        n (int): The number parameter from the URL.

    Returns:
        str: The rendered HTML template.
    '''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
