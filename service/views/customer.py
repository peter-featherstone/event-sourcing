from flask import render_template

from service import app


@app.route('/customer')
def customer():
    return render_template('customer.html')
