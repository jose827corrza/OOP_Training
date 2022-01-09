from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola de python")

    car =Car("BSC996", Account("Jose", "1015464260"))
    print(vars(car))
    print(vars(car.driver))

    