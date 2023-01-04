from app.employee.domain.Employee import Employee

import uuid


def test_employee_existing_id():
    test_id = str(uuid.uuid4().hex)

    assert Employee(name='Luis',id=test_id).id == test_id

def test_Employee_defaults():
    test_id = str(uuid.uuid4().hex)

    assert Employee(name='Juan').id != test_id