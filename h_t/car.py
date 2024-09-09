class Car:
    def __init__(self, brand, manuf_year, model, price, potential_price) -> None:
        self.brand = brand
        self.manuf_year = manuf_year
        self.model = model
        self.price = price
        self.potential_price = potential_price

    def __repr__(self) -> str:
        return f"{self.brand}, {self.manuf_year},{self.model}, {self.price}, {self.potential_price}"

    def profit_car(self, real_price):
        profit_car =real_price -  self.price 
        return profit_car


class CarSevice:
    _instance = None
    cars = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarSevice, cls).__new__(cls)
        return cls._instance

    def find_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car
        print("Car is not in the list")

    def add_car(self, brand, manuf_year, model, price, potential_price) -> None:
        car = Car(brand, manuf_year, model, price, potential_price)
        self.cars.append(car)

    def delete_car(self, model):
        self.cars.remove(self.find_car(model))
        print("Car has been deleted")

    def show_cars(self):
        for car in self.cars:
            print(car)
