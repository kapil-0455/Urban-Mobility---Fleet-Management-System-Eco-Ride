from vehicle import Vehicle
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


class EcoRideMain:
    def __init__(self):
        pass
    def run(self):
        print("Welcome to Eco-Ride Urban Mobility System\n")

        # Electric car
        e_car = ElectricCar("001", "Tesla Model 3", 85, "Excellent", 5000, 5)
        volvo_ev = ElectricCar("002", "Volvoc4", 92, "Excellent", 4500, 7)
        
        # Electric scooter
        e_scooter = ElectricScooter("003", "Ather 450X", 90, "Good", 1000, 90)
        ola_e_scooter = ElectricScooter("004", "Ola", 85, "Excellent", 1200, 85)
        

        # List of mixed vehicle objects
        vehicles = [e_car,volvo_ev ,e_scooter, ola_e_scooter]

        # Process rentals dynamically
        for vehicle in vehicles:
            print(vehicle)
            print(f"Trip Cost : {vehicle.calculate_trip_cost(30)}\n")


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
