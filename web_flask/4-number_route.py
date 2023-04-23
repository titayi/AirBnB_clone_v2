#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a string
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    Returns a string
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Returns a string
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns a String
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
