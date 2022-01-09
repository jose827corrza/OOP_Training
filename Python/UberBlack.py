from car import Car
#Herencia en Python, la clase importada es argumento de la clase hija
class UberBlack(Car):
    typeCarAccepted = []
    seatMaterial = []

    def __init__(self, licence, driver, typeCarAccepted, seatMaterial):
        super().__init__(licence, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterial = seatMaterial
        