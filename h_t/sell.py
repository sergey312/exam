from car import Car, CarSevice
from employee import Employee, EmployeeService
from datetime import datetime, timedelta
import random


class Sell:
    def __init__(self, employee: Employee, car: Car, date, real_price) -> None:
        self.employee = employee
        self.car = car
        self.date = date
        self.real_price = real_price

    def __repr__(self) -> str:
        return f"{self.employee.full_name} sold {self.car.brand} {self.car.model} {self.car.manuf_year} for {self.real_price}$, date is {self.date}"


class SellService:
    def __init__(self) -> None:
        self.sells = []
        self.employee_service = EmployeeService()
        self.car_service = CarSevice()

    def __return_sells_by_date_and_empl(self, date1,  date2, name_employee="all"):
        sells = []
        if date1:
            date1 = datetime.strptime(date1, "%d.%m.%Y")
        if date2:
            date2 = datetime.strptime(date2, "%d.%m.%Y")
        for sell in self.sells:
            if isinstance(sell.date, str):
                sell.date = datetime.strptime(sell.date, "%d.%m.%Y")
            if date1 and date2:
                if date1 <= sell.date <= date2:
                    if name_employee == "all" or sell.employee.full_name == name_employee:
                        sells.append(sell)
            elif date1:
                if sell.date.date() == date1.date():
                    if name_employee == "all" or sell.employee.full_name == name_employee:
                        sells.append(sell)
            elif name_employee != "all":
                if sell.employee.full_name == name_employee:
                    sells.append(sell)
            else:
                sells.append(sell)
        return sells

    def add_sell(self, full_name_employee, model, real_price):
        if isinstance(self.employee_service.find_employee(full_name_employee), Employee):
            employee = self.employee_service.find_employee(full_name_employee)
        else:
            raise TypeError("Employee is not in the list")
        if isinstance(self.car_service.find_car(model), Car):
            car = self.car_service.find_car(model)
        else:
            raise TypeError("Car is not in the list")
        date = generate_random_date("01.01.2020", "31.12.2024")
        # date = date.now()
        sell = Sell(employee, car, date, real_price)
        self.sells.append(sell)

    def delete_sell(self, full_name, model):
        for sell in self.sells:
            if sell.car.model == model and sell.employee.full_name == full_name:
                self.sells.remove(sell)
                print("Selling has been deleted")

    def show_sells(self, date1=None,  date2=None, name_employee="all"):
        sells = self.__return_sells_by_date_and_empl(
            date1, date2, name_employee)
        for sell in sells:
            print(sell)

    def show_profit(self, date=None):
        if date is None:
            profit = 0
            for sell in self.sells:
                profit = profit + sell.car.profit_car(sell.real_price)
            return f"The company profit is {profit}$"

    def __most_frequent_key(self, define, date1, date2):
        key_count = {}
        sells = self.__return_sells_by_date_and_empl(
            date1, date2)
        for sell in sells:
            if define == "car":
                key = sell.car.model
            else:
                key = sell.employee.full_name
            if key in key_count:
                key_count[key] += 1
            else:
                key_count[key] = 1
        if not key_count:
            return None
        most_common_key = max(key_count, key=key_count.get)
        if define == "car":
            car = self.car_service.find_car(most_common_key)
            return car
        else:
            employee = self.employee_service.find_employee(most_common_key)
            return employee

    def show_best_seller(self, key="employee", date1=None, date2=None):
        return self.__most_frequent_key(key, date1, date2)

    def show_most_purchased_car(self, key="car", date1=None, date2=None):
        return self.__most_frequent_key(key, date1, date2)

# for testing


def generate_random_date(start_date, end_date):
    start = datetime.strptime(start_date, "%d.%m.%Y")
    end = datetime.strptime(end_date, "%d.%m.%Y")

    delta = end - start
    random_days = random.randint(0, delta.days)

    random_date = start + timedelta(days=random_days)

    return random_date.strftime("%d.%m.%Y")
