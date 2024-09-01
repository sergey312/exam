class Employee:
    def __init__(self, full_name, role, telefon_number, email) -> None:
        self.full_name = full_name
        self.role = role
        self.telefon_number = telefon_number
        self.email = email


class Car:
    def __init__(self, brand, manuf_year, model, price, potential_price) -> None:
        self.brand = brand
        self.manuf_year = manuf_year
        self.model = model
        self.cost = price
        self.potential_cost = potential_price


class Sells:
    def __init__(self, employee: Employee, car: Car, date, real_price) -> None:
        self.employee = employee
        self.car = car
        self.date = date
        self.real_price = real_price
