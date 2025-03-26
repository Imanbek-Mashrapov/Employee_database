class Employee:
    def __init__(self, name, position, salary, hireDate, employeeId = None,):
        self.employeeId = employeeId
        self.name = name
        self.position = position
        self.salary = salary
        self.hireDate = hireDate

    def set_employeeId(self, id):
        self.employeeId = id

    def __str__(self):
        return f'ID: {self.employeeId}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hire date {self.hireDate} '





