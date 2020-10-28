"""Collection of view endpoints for main functionality."""
from flask import render_template

from service import app


@app.route('/')
def index():
    """UI endpoint to display the landing page."""
    return render_template('index.html')
