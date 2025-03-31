# Employee database

This project is a Python-based Employee Management System that interacts with an SQLite database. It allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records.

## Features
- #### SQLite Database: Stores employee details.
- #### Employee Class: Represents an employee with id, name, position, salary, hire_date.
- #### EmployeeDAO Class: Handles all database operations.
- #### CLI Menu: Allows users to manage employees interactively.
- #### Unit Testing: Ensures correct functionality of database operations

## Table structure
| Column     | Type      | Constraints                     |
|------------|----------|--------------------------------|
| `id`       | INTEGER  | PRIMARY KEY, AUTO-INCREMENT   |
| `name`     | TEXT     | NOT NULL                       |
| `position` | TEXT     | NOT NULL                       |
| `salary`   | REAL     | NOT NULL                       |
| `hire_date`| TEXT     | NOT NULL (YYYY-MM-DD format)  |

## Input/Output examples
### How the program works:

```ssh
    <Employee database>
    1. Add employee
    2. Delete employee by id
    3. See all employees
    4. Get employee by id
    5. Update employee information by id
    6. Delete all employees
    7. Exit
    Choose the action:
```

### 1. Adding
#### Input
```python
Choose the action: 1
Enter employee's info (id, name, position, salary, hire date YYYY-MM-DD): 1, Iman Mashrapov, Data Scientist, 50000, 2024-07-07
```
#### Output
```ssh
Employee added
```

### 2. Deleting employee
#### Input
```python
Choose the action: 2
Enter employee id to delete: 6
```
#### Output
```ssh
Employee with id:6 was deleted
```

### 3. Viewing All Employees
#### Input
```python
Choose the action: 3
```
#### Output
```ssh
ID: 1, Name: Iman Mashrapov, Position: Data Scientist, Salary: 50000.0, Hire date: 2024-07-07
ID: 2, Name: Aman Usenov, Position: Manager, Salary: 60000.0, Hire date: 2024-01-01
ID: 3, Name: Maksat Aliev, Position: Devops Engineer, Salary: 50000.0, Hire date: 2024-01-20
ID: 4, Name: Danil Janyshev, Position: Ui-Ux Designer, Salary: 45000.0, Hire date: 2023-05-01
ID: 5, Name: Nurbek Sultanaliev, Position: Database administrator, Salary: 52000.0, Hire date: 2023-04-25
```

### 4. Getting an Employee by ID
#### Output
```python
Choose the action: 4
Enter employee id to get: 1
```
#### Output
```ssh
Employee Details:
ID: 1, Name: Iman Mashrapov, Position: Data Scientist, Salary: 50000.0, Hire date: 2024-07-07
```

### 5. Updating an employee 
#### Input
```python
Choose the action: 5
Enter employee id to update: 1
Enter new employee info (name, position, salary, hire date YYYY-MM-DD): Imanbek Mashrapov, ML engineer, 60000, 2024-07-07
```
#### Output
```ssh
Employee info was modified
```

### 6. Deleting all employees
#### Input
```python
Choose the action: 6
Are you sure you want to delete ALL employees? (yes/no): yes
```
#### Output
```ssh
All employees were deleted
```

### 7. Exiting the program
#### Input
```python
Choose the action: 7
```
#### Output
```ssh
Process finished with exit code 0
```








