#!/usr/bin/python3
"""
A simple Flask web application.
"""
from flask import Flask


app = Flask(__name__)
"""
The Flask application instance.
"""
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    The home page.

    Returns:
        str: The message displayed on the home page.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    The HBNB page.

    Returns:
        str: The message displayed on the HBNB page.
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    """
    The C page.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The formatted message displaying the provided text.
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
