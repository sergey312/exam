from car import Car
from employee import Employee
from sell import Sell


class Managment:
    def __init__(self) -> None:
        self.sells = []
        self.cars = []
        self.employees = []

    def add_employee(self, full_name, role, telefon_number, email) -> None:
        employee = Employee(full_name, role, telefon_number, email)
        self.employees.append(employee)

    def delete_employee(self, full_name) -> None:
        for employee in self.employees:
            if employee.full_name == full_name:
                self.employees.remove(employee)
                print("Employee has been deleted")

    def add_car(self, brand, manuf_year, model, price, potential_price) -> None:
        car = Car(brand, manuf_year, model, price, potential_price)
        self.cars.append(car)

    def delete_car(self, model):
        for car in self.cars:
            if car.model == model:
                self.cars.remove(car)
                print("Employee has been deleted")

    def add_sell(self):
        pass

    def delete_sell(self):
        pass

    def show_employees(self):
        for employee in self.employees:
            print(employee)

    def show_cars(self):
        for car in self.cars:
            print(car)

    def show_sells(self, date="all", employee="all"):
        pass

    def show_besteler_car(self, date):
        pass

    def show_best_seller(self, date):
        pass

    def show_profit(self, date):
        pass
