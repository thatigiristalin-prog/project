
from employee import employees, add_employee, search_employee, update_salary, delete_employee


def setup_function():
    employees.clear()


def test_add_employee():
    assert add_employee("101", "Rahul", 30000) == "Employee Added Successfully"


def test_search_employee():
    add_employee("101", "Rahul", 30000)
    assert search_employee("101") == ["101", "Rahul", 30000]


def test_update_salary():
    add_employee("101", "Rahul", 30000)
    assert update_salary("101", 35000) == "Salary Updated"


def test_delete_employee():
    add_employee("101", "Rahul", 30000)
    assert delete_employee("101") == "Employee Deleted"


def test_employee_not_found():
    assert search_employee("999") == "Employee Not Found"
