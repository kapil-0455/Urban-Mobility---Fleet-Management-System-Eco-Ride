from vehicle import Vehicle
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class EcoRideMain:
    def __init__(self):
        pass
    def run(self) :
        print("Welcome to Eco-Ride Urban Mobility System\n")

        # Vehicle
        car = Vehicle("001", "Scorpio S11", 30, "Good", 2500)
        print("Testing Vehicle details:")
        print(car)

        # updating
        car.set_battery_percentage(80)
        car.set_rental_price(3000)
        print("After Update:")
        print(car)

        # Electric car
        e_car = ElectricCar("002", "Tesla Model 3", 85, "Excellent", 5000, 5)
        print("\nTesting ElectricCar details:")
        print(e_car)

        # Electric scooter
        e_scooter = ElectricScooter("003", "Ather 450X", 90, "Good", 1000, 90)
        print("\nTesting ElectricScooter details:")
        print(e_scooter)


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
