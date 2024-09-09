from sell import SellService
from car import CarSevice
from employee import EmployeeService


class Managment:
    def __init__(self) -> None:
        self.sell_service = SellService()
        self.car_sevice = CarSevice()
        self.employee_service = EmployeeService()
