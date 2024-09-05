from car import Car
from employee import Employee
from sell import Sell
import time


class Managment:
    def __init__(self) -> None:
        self.sells = []
        self.cars = []
        self.employees = []

    def add_employee(self, full_name, role, telefon_number, email) -> None:
        employee = Employee(full_name, role, telefon_number, email)
        self.employees.append(employee)

    def __find_employee(self, full_name):
        for employee in self.employees:
            if employee.full_name == full_name:
                return employee
        print("Employee is not in the list")

    def __find_car(self, brand, model):
        for car in self.cars:
            if car.model == model and car.brand == brand:
                return car
        print("Car is not in the list")

    def delete_employee(self, full_name) -> None:
        self.employees.remove(self.__find_employee(full_name))
        print("Employee has been deleted")

    def add_car(self, brand, manuf_year, model, price, potential_price) -> None:
        car = Car(brand, manuf_year, model, price, potential_price)
        self.cars.append(car)

    def delete_car(self, brand, model):
        self.cars.remove(self.__find_car(brand, model))
        print("Car has been deleted")

    def add_sell(self, full_name_employee, brand, model, real_price):
        if isinstance(self.__find_employee(full_name_employee), Employee):
            employee = self.__find_employee(full_name_employee)
        else:
            raise TypeError("Employee is not in the list")
        if isinstance(self.__find_car(brand, model), Car):
            car = self.__find_car(brand, model)
        else:
            raise TypeError("Car is not in the list")
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        sell = Sell(employee, car, date, real_price)
        self.sells.append(sell)

    def delete_sell(self):
        pass

    def show_employees(self):
        for employee in self.employees:
            print(employee)

    def show_cars(self):
        for car in self.cars:
            print(car)

    def show_sells(self, date="all", employee="all"):
        for sell in self.sells:
            print(sell)

    def show_besteler_car(self, date):
        pass

    def show_best_seller(self, date):
        pass

    def show_profit(self, date):
        pass
