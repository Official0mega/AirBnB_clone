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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
