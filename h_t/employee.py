class Employee:
    def __init__(self, full_name, role, telefon_number, email) -> None:
        self.full_name = full_name
        self.role = role
        self.telefon_number = telefon_number
        self.email = email

    def __repr__(self) -> str:
        return f"{self.full_name}, {self.role}, {self.telefon_number}, {self.email}"


class EmployeeService:
    _instance = None
    employees = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmployeeService, cls).__new__(cls)
        return cls._instance

    def add_employee(self, full_name, role, telefon_number, email) -> None:
        employee = Employee(full_name, role, telefon_number, email)
        self.employees.append(employee)

    def add_employee(self, full_name, role, telefon_number, email) -> None:
        employee = Employee(full_name, role, telefon_number, email)
        self.employees.append(employee)

    def find_employee(self, full_name):
        for employee in self.employees:
            if employee.full_name == full_name:
                return employee
        print("Employee is not in the list")

    def delete_employee(self, full_name) -> None:
        self.employees.remove(self.find_employee(full_name))
        print("Employee has been deleted")

    def show_employees(self):
        for employee in self.employees:
            print(employee)
