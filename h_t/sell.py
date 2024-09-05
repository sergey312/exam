from car import Car
from employee import Employee


class Sell:
    def __init__(self, employee: Employee, car: Car, date, real_price) -> None:
        self.employee = employee
        self.car = car
        self.date = date
        self.real_price = real_price
