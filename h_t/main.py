from managment import Managment


def main():

    managment = Managment()
    managment.employee_service.add_employee("Andrii Hmelnitski", "Seller",
                                            "+380123123321", "faskdh@gamil.com")
    managment.employee_service.add_employee("Serhii Krolinski", "Seller",
                                            "+380123123321", "faskdh@gamil.com")
    managment.employee_service.add_employee("Nikolai", "Manager",
                                            "+380123123321", "faskdh@gamil.com")
    managment.employee_service.add_employee("Denis", "Konsoltant",
                                            "+380123123321", "faskdh@gamil.com")
    # managment.employee_service.show_employees()
    managment.employee_service.delete_employee("Andrii Hmelnitski")
    # managment.employee_service.show_employees()
    managment.car_sevice.add_car("Toyota", 2020, "Camry", 20000, 25000)
    managment.car_sevice.add_car("Honda", 2019, "Civic", 18000, 23000)
    managment.car_sevice.add_car("Ford", 2021, "Mustang", 35000, 40000)
    managment.car_sevice.add_car("Chevrolet", 2020, "Malibu", 22000, 27000)
    managment.car_sevice.add_car("BMW", 2022, "X5", 60000, 70000)
    managment.car_sevice.add_car("Audi", 2021, "A4", 40000, 45000)
    managment.car_sevice.add_car("Mercedes", 2018, "C-Class", 35000, 40000)
    managment.car_sevice.add_car("Nissan", 2019, "Altima", 20000, 25000)
    managment.car_sevice.add_car("Tesla", 2022, "Model 3", 45000, 55000)
    managment.car_sevice.add_car("Volkswagen", 2020, "Passat", 25000, 30000)
    # managment.car_sevice.show_cars()
    managment.car_sevice.delete_car("A4")
    # managment.car_sevice.show_cars()
    managment.sell_service.add_sell(
        "Serhii Krolinski", "Model 3", 75000)
    managment.sell_service.add_sell(
        "Nikolai", "Altima", 25000)
    managment.sell_service.add_sell(
        "Serhii Krolinski", "X5", 55000)

    managment.sell_service.add_sell(
        "Nikolai", "X5", 85000)
    managment.sell_service.show_sells()
    managment.sell_service.delete_sell("Nikolai", "Altima")
    managment.sell_service.show_sells()
    # print(managment.sell_service.show_profit())
    # print(managment.sell_service.show_best_seller())
    # print(managment.sell_service.show_most_purchased_car())


if __name__ == "__main__":
    main()
