class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}"

    def honk(self):
        return "Транспортний засіб сигналить!"


class Car(Transport):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()}, Тип пального: {self.fuel_type}"

    def honk(self):
        return "Біп-біп!"


class Bicycle(Transport):
    def __init__(self, brand, model, year, gear_count):
        super().__init__(brand, model, year)
        self.gear_count = gear_count

    def get_info(self):
        return f"{super().get_info()}, Кількість передач: {self.gear_count}"

    def honk(self):
        
        return "Дзинь-дзинь!"



if __name__ == "__main__":
   
    car = Car("Bmw", "m4cs", 2020, "Бензин")
    bicycle = Bicycle("Giant", "Escape 3", 2021, 21)

    print(car.get_info())
    print(car.honk())

    print(bicycle.get_info())
    print(bicycle.honk())