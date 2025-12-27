# hierarchy = {"CEO": {"Manager1": {"Employee1": { 'id': 1,'name': 'Employee1', 'department': 'HR' }, "Employee2": { 'id': 2,'name': 'Employee2', 'department': 'HR' }},"Manager2": {"Employee3": { 'id': 3,'name': 'Employee3', 'department': 'HR' }, "Employee4": { 'id': 4,'name': 'Employee4', 'department': 'HR' }}}}

import json

def main():

    print("Enter the hierarchy:")
    hierarchy = json.loads(input())

    print("Enter the employee id to find department:")
    employee_id = int(input())

    department = next((
        employee['department']
        for managers in hierarchy.values()
        for employees in managers.values()
        for employee in employees.values()
        if employee['id'] == employee_id
    ), "Employee not found")
    
    print(department)
    
main()