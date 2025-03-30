from employee_class import Employee
from employee_DAO import EmployeeDAO


if __name__ == "__main__":
    dao = EmployeeDAO()

    emp1 = Employee(1, "Iman Mashrapov", "Data Analyst", 75000, "2024-07-07")
    emp2 = Employee(2, "Abai Nurlanov", "Data Scientist", 95000, "2024-07-07")
    emp3 = Employee(3, "Baisal Zamirbek uulu", "Data Engineer", 78000, "2024-07-07")

    dao.insert(emp1)
    dao.insert(emp2)
    dao.insert(emp3)
    print("Employees inserted to db")

    all_emps = dao.get_all()
    print("All employees:")
    for e in all_emps:
        print(e)

    print("Employee with id:1 is: ")
    print(dao.get_by_id(1))

    new_emp = Employee(1, 'Imanbek Mashrapov', 'Financial Analyst', 80000, '2025-03-01')
    dao.update(1, new_emp)
    print("Updated employee:")
    print(dao.get_by_id(1))

    dao.delete(1)
    print("Deleted employee with id: 1")
    for e in dao.get_all():
        print(e)

    dao.close()
