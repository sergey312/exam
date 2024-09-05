
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
    managment.show_employees()
    managment.delete_employee("Andrii Hmelnitski")
    managment.show_employees()


if __name__ == "__main__":
    main()
