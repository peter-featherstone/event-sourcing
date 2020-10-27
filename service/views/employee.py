import random

from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from service import app
from service.repos import get_employee_repo


@app.route('/employee/<employee_id>', methods=['GET'])
def employee(employee_id):
    employee_repo = get_employee_repo()
    employee = employee_repo.get(_id=employee_id)

    return render_template('employee.html', employee=employee)


@app.route('/employees/', methods=['GET'])
def employees():
    employee_repo = get_employee_repo()
    employees = employee_repo.all()

    return render_template('employees.html', employees=employees)


@app.route('/employee/<employee_id>', methods=['POST'])
def employee_update(employee_id):
    employee_repo = get_employee_repo()
    employee = employee_repo.get(_id=employee_id)

    employee_id = random.randint(1, 101)

    if request.form['job']:
        employee.change_job(job=request.form['job'])

    if request.form['name']:
        employee.change_name(name=request.form['name'])

    if request.form['salary']:
        employee.change_salary(salary=request.form['salary'])

    employee_repo.save(entity=employee)

    return redirect(url_for('employee', employee_id=employee_id))
