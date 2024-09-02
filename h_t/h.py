class Employee:
    def __init__(self, full_name, role, telefon_number, email) -> None:
        self.full_name = full_name
        self.role = role
        self.telefon_number = telefon_number
        self.email = email

    def __repr__(self) -> str:
        return f"{self.full_name}, {self.role}, {self.telefon_number}, {self.email}"


class Car:
    def __init__(self, brand, manuf_year, model, price, potential_price) -> None:
        self.brand = brand
        self.manuf_year = manuf_year
        self.model = model
        self.cost = price
        self.potential_cost = potential_price


class Sell:
    def __init__(self, employee: Employee, car: Car, date, real_price) -> None:
        self.employee = employee
        self.car = car
        self.date = date
        self.real_price = real_price


class Managment:
    def __init__(self) -> None:
        self.sells = []
        self.cars = []
        self.employees = []

    def add_employee(self, full_name, role, telefon_number, email):
        employee = Employee(full_name, role, telefon_number, email)
        self.employees.append(employee)

    def delete_employee(self, full_name):
        for employee in self.employees:
            if employee.full_name == full_name:
                self.employees.remove(employee)
                print("Employee has been deleted")

    def add_car(self):
        pass

    def delete_car(self):
        pass

    def add_sell(self):
        pass

    def delete_sell(self):
        pass

    def show_employees(self):
        for employee in self.employees:
            print(employee)

    def show_cars(self):
        pass

    def show_sells(self, date="all", employee="all"):
        pass

    def show_besteler_car(self, date):
        pass

    def show_best_seller(self, date):
        pass

    def show_profit(self, date):
        pass


class Files:
    pass


def main():
    managment = Managment()
    managment.add_employee("Andrii Hmelnitski", "Seller",
                           "+380123123321", "faskdh@gamil.com")
    managment.add_employee("Serhii Krolinski", "Seller",
                           "+380123123321", "faskdh@gamil.com")
    managment.add_employee("Nikolai", "Manager",
                           "+380123123321", "faskdh@gamil.com")
    managment.add_employee("Denis", "Konsoltant",
                           "+380123123321", "faskdh@gamil.com")
    managment.show_employees()
    managment.delete_employee("Andrii Hmelnitski")
    managment.show_employees()


if __name__ == "__main__":
    main()
