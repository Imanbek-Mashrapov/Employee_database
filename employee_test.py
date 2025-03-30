import unittest
from employee_class import Employee
from employee_DAO import EmployeeDAO


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee(1, "Iman Mashrapov", "Data Analyst", 75000, "2024-07-07")

    def test_set_id(self):
        new_id = 10
        self.emp1.id = new_id
        self.assertEqual(new_id, self.emp1.id)


class TestEmployeeDAO(unittest.TestCase):
    def setUp(self):
        self.emp_dao = EmployeeDAO()
        self.emp_dao.cursor.execute("DELETE FROM employee")
        self.emp_dao.conn.commit()
        self.emp1 = Employee(1, "Iman Mashrapov", "Data Analyst", 75000, "2021-05-03")
        self.emp2 = Employee(None, "Ruslan Talgatov", "Project Manager", 70000, "2022-03-30")
        self.emp3 = Employee(None, "Sanjar Amirov", "Police officer", 90000, "2010-01-25")

    def test_insert(self):
        self.emp_dao.insert(self.emp1)
        self.emp_dao.insert(self.emp2)
        self.emp_dao.insert(self.emp3)
        employees = self.emp_dao.get_all()
        self.assertTrue(any(emp.name == self.emp1.name for emp in employees))
        self.assertTrue(any(emp.name == self.emp2.name for emp in employees))
        self.assertTrue(any(emp.name == self.emp3.name for emp in employees))

    def test_get_by_id(self):
        self.emp_dao.insert(self.emp1)
        emp = self.emp_dao.get_by_id(1)
        self.assertIsNotNone(emp)
        self.assertEqual(emp.name, self.emp1.name)

    def test_update(self):
        self.emp_dao.insert(self.emp1)
        emp = self.emp_dao.get_by_id(1)
        emp.name = "Omurbek"
        self.emp_dao.update(emp)
        updated_emp = self.emp_dao.get_by_id(1)
        self.assertEqual(updated_emp.name, "Omurbek")

    def test_delete(self):
        self.emp_dao.insert(self.emp1)
        self.emp_dao.delete(1)
        self.assertIsNone(self.emp_dao.get_by_id(1))






