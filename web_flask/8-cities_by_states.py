#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    Closes current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays a HTML page with a list of all State objects present in DBStorage sorted by name (A->Z)
    and a list of City objects linked to the State sorted by name (A->Z)
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
