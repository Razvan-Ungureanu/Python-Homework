class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand: str, year: int, fuel_type: str):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Fuel: {self.fuel_type}")


car = Car("Toyota", 1949, "petrol")
car.display_info()