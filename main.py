from employee_class import Employee
from employee_DAO import EmployeeDAO


if __name__ == "__main__":
    dao = EmployeeDAO()

    emp1 = Employee(1, "Iman Mashrapov", "Data Analyst", 75000, "2024-07-07")
    dao.insert(emp1)
    print("Employee inserted.")

    emp = dao.get_by_id(1)
    if emp:
        print("Retrieved employee:", emp)

    all_emps = dao.get_all()
    print("All Employees:")
    for e in all_emps:
        print(e)

    if emp:
        emp.name = "Jane Doe"
        dao.update(emp)
        print("Updated employee:", dao.get_by_id(emp.id))

    dao.delete(1)
    print("Deleted employee with ID 1.")

    dao.close()
