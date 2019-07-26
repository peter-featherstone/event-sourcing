import random

from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from service import app
from service.repos import get_customer_repo


@app.route('/customer/<customer_id>', methods=['GET'])
def customer(customer_id):
    customer_repo = get_customer_repo()
    customer = customer_repo.get(_id=customer_id)

    return render_template('customer.html', customer=customer)


@app.route('/customers/', methods=['GET'])
def customers():
    customer_repo = get_customer_repo()
    customers = customer_repo.all()

    return render_template('customers.html', customers=customers)


@app.route('/customer/<customer_id>', methods=['POST'])
def customer_update(customer_id):
    customer_repo = get_customer_repo()
    customer = customer_repo.get(_id=customer_id)

    user_id = random.randint(1, 101)

    if request.form['job']:
        customer.change_job(job=request.form['job'], user_id=user_id)

    if request.form['name']:
        customer.change_name(name=request.form['name'], user_id=user_id)

    if request.form['salary']:
        customer.change_salary(salary=request.form['salary'], user_id=user_id)

    customer_repo.save(entity=customer)

    return redirect(url_for('customer', customer_id=customer_id))
