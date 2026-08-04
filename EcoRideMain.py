from vehicle import Vehicle
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class EcoRideMain:
    def __init__(self):
        pass
    def run(self) :
        print("Welcome to Eco-Ride Urban Mobility System")
        # Electric car
        e_car = ElectricCar("001", "Tesla Model 3", 85, "Excellent", 5000, 5)
        print("\nTesting ElectricCar details:")
        print(e_car)
        print(f"Trip Cost : {e_car.calculate_trip_cost(30)}")

        # Electric scooter
        e_scooter = ElectricScooter("002", "Ather 450X", 90, "Good", 1000, 90)
        print("\nTesting ElectricScooter details:")
        print(e_scooter)
        print(f"Trip Cost : {e_scooter.calculate_trip_cost(15)}")


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
