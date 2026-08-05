from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from fleet_manager import FleetManager


class EcoRideMain:
    def __init__(self):
        pass
    def run(self):

        print("Welcome to Eco-Ride Urban Mobility System")

        fleet = FleetManager()
        while True:

            try:
                choice = int(input(
                    "\n========== Eco Ride Menu ==========\n"
                    "1. Add Hub\n"
                    "2. Add Vehicle to Hub\n"
                    "3. Display Hubs\n"
                    "4. Remove Vehicle from Hub\n"
                    "5. Exit\n"
                    "Enter your choice: "
                ))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                hub_name = input("Enter Hub Name: ")
                fleet.add_hub(hub_name)

            elif choice == 2:

                hub_name = input("Enter Hub Name: ")

                try:
                    vehicle_choice = int(input(
                        "\nVehicle Type\n"
                        "1. Electric Car\n"
                        "2. Electric Scooter\n"
                        "Enter choice: \n"
                    ))
                except ValueError:
                    print('Invalid vehicle choice')

                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                maintenance_choice = int(input(
                    "\nMaintenance Status\n"
                    "1. Available\n"
                    "2. Under Maintenance\n"
                    "3. Out of Service\n"
                    "Enter choice: "
                ))

                if maintenance_choice == 1:
                    maintenance = "Available"

                elif maintenance_choice == 2:
                    maintenance = "Under Maintenance"

                elif maintenance_choice == 3:
                    maintenance = "Out of Service"

                else:
                    print("Invalid Maintenance Status.")
                    continue

                try:
                    battery = int(input("Enter Battery Percentage: "))
                    rental_price = float(input("Enter Rental Price: "))
                except ValueError:
                    print("Battery percentage and Rental Price must be numeric.")
                    continue

                if vehicle_choice == 1:
                    try:
                        seating_capacity = int(input("Enter Seating Capacity: "))
                        vehicle = ElectricCar(vehicle_id,model,battery,maintenance,rental_price,seating_capacity)
                        fleet.add_vehicle_to_hub(hub_name, vehicle)
                    except ValueError as e:
                        print(e)

                elif vehicle_choice == 2:
                    try:
                        max_speed = int(input("Enter Max Speed Limit: "))
                        vehicle = ElectricScooter(vehicle_id,model,battery,maintenance,rental_price,max_speed)
                        fleet.add_vehicle_to_hub(hub_name, vehicle)
                    except ValueError as e:
                        print(e)

                else:
                    print("Invalid Vehicle Type.")

            elif choice == 3:
                fleet.display_hubs()

            elif choice == 4:
                hub_name = input("Enter Hub Name: ")
                vehicle_id = input("Enter Vehicle ID: ")
                fleet.remove_vehicle_to_hub(hub_name , vehicle_id)

            elif choice == 5 :
                print('Thank you')
                break

            else :
                print('Choice is Invalid please try again')


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
