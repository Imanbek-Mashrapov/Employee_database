from employee_class import Employee
import sqlite3


class EmployeeDAO:
    def __init__(self, db_name="employee_db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert(self, employee: Employee):
        self.cursor.execute('''
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        ''', (employee.name, employee.position, employee.salary, employee.hireDate))
        self.conn.commit()

    def get_by_id(self, emp_id):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (emp_id,))
        row = self.cursor.fetchone()
        if row:
            return Employee(*row)
        return None

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update(self, employee: Employee):
        self.cursor.execute('''
            UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        ''', (employee.name, employee.position, employee.salary, employee.hireDate, employee.employeeId))
        self.conn.commit()

    def delete(self, emp_id):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()











