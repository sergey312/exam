class Car:
    def __init__(self, brand, manuf_year, model, price, potential_price) -> None:
        self.brand = brand
        self.manuf_year = manuf_year
        self.model = model
        self.price = price
        self.potential_price = potential_price

    def __repr__(self) -> str:
        return f"{self.brand}, {self.manuf_year},{self.model}, {self.price}, {self.potential_price}"
