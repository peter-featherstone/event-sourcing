"""Collection of view endpoints for dealing with employees."""
from uuid import uuid4

from flask import redirect, render_template, request, url_for, flash

from service import app
from service.models.employee.employee import Employee
from service.repos import get_employee_repo


@app.route('/employee/create', methods=['GET'])
def create_employee_form():
    """UI endpoint to display a create new employee form."""
    return render_template('create_employee.html')


@app.route('/employee/<employee_id>', methods=['GET'])
def employee(employee_id):
    """UI endpoint to display an individual employees details."""
    employee_repo = get_employee_repo()
    employee = employee_repo.get(id_=employee_id)

    return render_template('employee.html', employee=employee)


@app.route('/employees', methods=['GET'])
def employees():
    """UI endpoint to display a list of all employees in the system."""
    employee_repo = get_employee_repo()
    employees = employee_repo.all()

    return render_template('employees.html', employees=employees)


@app.route('/employee', methods=['POST'])
def create_employee():
    """Internal endpoint used for the creation of new employees."""
    employee = Employee(id_=uuid4())
    employee.create(
        name=request.form['name'],
        job=request.form['job'],
        salary=int(request.form['salary'])
    )

    employee_repo = get_employee_repo()
    employee_repo.save(entity=employee)

    flash(message=f'{employee.name} created.')

    return redirect(url_for('employee', employee_id=employee.id))


@app.route('/employee/<employee_id>', methods=['POST'])
def update_employee(employee_id):
    """Internal endpoint for updating an employees data."""
    employee_repo = get_employee_repo()
    employee = employee_repo.get(id_=employee_id)

    if request.form['job']:
        employee.change_job(job=request.form['job'])

    if request.form['name']:
        employee.change_name(name=request.form['name'])

    if request.form['salary']:
        employee.change_salary(salary=int(request.form['salary']))

    employee_repo.save(entity=employee)

    flash(message=f'{employee.name} updated.')

    return redirect(url_for('employee', employee_id=employee_id))
