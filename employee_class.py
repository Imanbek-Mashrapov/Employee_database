class Employee:
    def __init__(self, id, name, position, salary, hireDate):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hireDate = hireDate

    def set_id(self, new_id):
        self.id = new_id

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hire date: {self.hireDate}"





