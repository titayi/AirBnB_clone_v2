#!/usr/bin/python3
"""
Starts a Flask web application with routes to display a list of all states
and to display details of a specific state.
"""

from flask import Flask, render_template
from models import storage, State, City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a list of all states."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_details(id):
    """Display details of a specific state."""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-not_found.html')
    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('9-state.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
