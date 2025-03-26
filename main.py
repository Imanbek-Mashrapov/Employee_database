from employee_class import Employee
from employee_DAO import EmployeeDAO


if __name__ == "__main__":
    dao = EmployeeDAO()

    # Insert an employee
    emp1 = Employee(None, "John Doe", "Software Engineer", 75000, "2024-07-07")
    dao.insert(emp1)
    print("Employee inserted.")

    # Retrieve an employee by ID
    emp = dao.get_by_id(1)
    if emp:
        print("Retrieved employee:", emp)

    # Retrieve all employees
    all_emps = dao.get_all()
    print("All Employees:")
    for e in all_emps:
        print(e)

    # Update an employee
    if emp:
        emp.name = "Jane Doe"
        dao.update(emp)
        print("Updated employee:", dao.get_by_id(emp.id))

    # Delete an employee
    dao.delete(1)
    print("Deleted employee with ID 1.")

    # Close the connection
    dao.close()
