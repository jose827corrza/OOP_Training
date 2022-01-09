from car import Car
#Herencia en Python, la clase importada es argumento de la clase hija
class UberPool(Car):
    brand = str
    model = str

    def __init__(self, licence, driver, brand, model):
        super().__init__(licence, driver)
        self.brand = brand
        self.model = model