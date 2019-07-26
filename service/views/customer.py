from flask import render_template

from service import app
from service.repos import get_customer_repo


@app.route('/customer')
def customer():
    customer_repo = get_customer_repo()
    customer = customer_repo.get(_id=1)

    return render_template('customer.html', customer=customer)
