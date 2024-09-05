
from managment import Managment


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
    # managment.show_employees()
    managment.delete_employee("Andrii Hmelnitski")
    # managment.show_employees()
    managment.add_car("Toyota", 2020, "Camry", 20000, 25000)
    managment.add_car("Honda", 2019, "Civic", 18000, 23000)
    managment.add_car("Ford", 2021, "Mustang", 35000, 40000)
    managment.add_car("Chevrolet", 2020, "Malibu", 22000, 27000)
    managment.add_car("BMW", 2022, "X5", 60000, 70000)
    managment.add_car("Audi", 2021, "A4", 40000, 45000)
    managment.add_car("Mercedes", 2018, "C-Class", 35000, 40000)
    managment.add_car("Nissan", 2019, "Altima", 20000, 25000)
    managment.add_car("Tesla", 2022, "Model 3", 45000, 55000)
    managment.add_car("Volkswagen", 2020, "Passat", 25000, 30000)
    # managment.show_cars()
    managment.delete_car("Audi", "A4")
    # managment.show_cars()
    managment.add_sell("Serhii Krolinski", "Tesla", "Model 3", 55000)
    managment.show_sells()


if __name__ == "__main__":
    main()
