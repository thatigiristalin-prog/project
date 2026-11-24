
import sys

employees = []

def add_employee(emp_id, name, salary):
    employees.append([emp_id, name, salary])
    return "Employee Added Successfully"

def display_employee():
    return employees

def search_employee(emp_id):
    for emp in employees:
        if emp[0] == emp_id:
            return emp
    return "Employee Not Found"

def update_salary(emp_id, salary):
    for emp in employees:
        if emp[0] == emp_id:
            emp[2] = salary
            return "Salary Updated"
    return "Employee Not Found"

def delete_employee(emp_id):
    for emp in employees:
        if emp[0] == emp_id:
            employees.remove(emp)
            return "Employee Deleted"
    return "Employee Not Found"


if __name__ == "__main__":
    choice = sys.argv[1]

    if choice == "add":
        print(add_employee(sys.argv[2], sys.argv[3], int(sys.argv[4])))
    elif choice == "display":
        print(display_employee())
    elif choice == "search":
        print(search_employee(sys.argv[2]))
    elif choice == "update":
        print(update_salary(sys.argv[2], int(sys.argv[3])))
    elif choice == "delete":
        print(delete_employee(sys.argv[2]))
    else:
        print("Invalid Choice")
