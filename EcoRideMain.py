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
                    "5. Search Vehicles\n"
                    "6. Fleet anayltics\n"
                    "7. Sort vehicle by Model in an Hub\n"
                    "8. Advanced Sorting (Battery/Price)\n"
                    "9. Exit\n"
                    "Enter your choice: "
                ))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                hub_name = input("Enter a hub name : ")
                try:
                    fleet.add_hub(hub_name)
                except ValueError as e:
                    print(e)

            elif choice == 2:

                hub_name = input("Enter Hub Name: ").strip()
                if not hub_name:
                    print("Hub name cannot be empty.")
                    continue

                while True:
                    print('================Vehicle choice =================')
                    try:
                        vehicle_choice = int(input(
                            "\nVehicle Type\n"
                            "1. Electric Car\n"
                            "2. Electric Scooter\n"
                            "Enter choice: "
                        ))
                        if vehicle_choice not in [1, 2]:
                            print("Please enter 1 or 2.")
                            continue
                    except ValueError:
                        print('Invalid vehicle choice. Please enter a number.')
                        continue

                    vehicle_id = input("Enter Vehicle ID: ").strip()
                    if not vehicle_id:
                        print("Vehicle ID cannot be empty.")
                        continue

                    model = input("Enter Model: ").strip()
                    if not model:
                        print("Model cannot be empty.")
                        continue

                    while True:
                        try:
                            maintenance_choice = int(input(
                                "\n===Maintenance Status====\n"
                                "1. Available\n"
                                "2. Under Maintenance\n"
                                "3. On Trip\n"
                                "Enter choice: "
                            ))
                        except ValueError :
                            print("Please enter a valid number.")
                            continue

                        if maintenance_choice == 1:
                            maintenance = "Available"
                            break
                        elif maintenance_choice == 2:
                            maintenance = "Under Maintenance"
                            break
                        elif maintenance_choice == 3:
                            maintenance = "On Trip"
                            break
                        else:
                            print("Invalid Maintenance Status.")
                            continue

                    if vehicle_choice == 1:
                        while True:
                            try:
                                battery = int(input("Enter Battery Percentage: "))
                                rental_price = float(input("Enter Rental Price: "))
                                seating_capacity = int(input("Enter Seating Capacity: "))
                                vehicle = ElectricCar(vehicle_id, model, battery, maintenance, rental_price, seating_capacity)
                                fleet.add_vehicle_to_hub(hub_name, vehicle)
                                break
                            except ValueError as e:
                                print(f"Error: {e} Please enter the values again.")
                        break

                    elif vehicle_choice == 2:
                        while True:
                            try:
                                battery = int(input("Enter Battery Percentage: "))
                                rental_price = float(input("Enter Rental Price: "))
                                max_speed = int(input("Enter Max Speed Limit: "))
                                vehicle = ElectricScooter(vehicle_id, model, battery, maintenance, rental_price, max_speed)
                                fleet.add_vehicle_to_hub(hub_name, vehicle)
                                break
                            except ValueError as e:
                                print(f"Error: {e} Please enter the values again.")
                        break


            elif choice == 3:
                fleet.display_hubs()

            elif choice == 4:
                hub_name = input("Enter Hub Name: ")
                vehicle_id = input("Enter Vehicle ID: ")
                try:
                    fleet.remove_vehicle_to_hub(hub_name, vehicle_id)
                except ValueError as e:
                    print(e)

            elif choice == 5 :
                while True:
                    try:
                        search_option = int(input(
                            "\n======= Search Option =======\n"
                            "1. Search by hub name\n"
                            "2. Search by battery\n"
                            "3. Exit search menu\n"
                            "Enter choice: "
                        ))
                    except ValueError:
                        print("Enter a valid Number ")
                        continue

                    if search_option == 1:
                        hub_name = input('Enter a hub Name : ')
                        fleet.search_by_hub(hub_name)
                    elif search_option == 2:
                        fleet.search_by_battery()
                    elif search_option == 3:
                        break
                    else :
                        print("Invalid choice. Please try again.")

            elif choice == 6:
                fleet.fleet_analytics()
                
            elif choice == 7 :
                hub_name = input("Enter hub name: ")
                fleet.alphabet_sort(hub_name)
            
            elif choice == 8:
                hub_name = input("Enter Hub Name: ")
                while True:
                    try:
                        sort_choice = int(input(
                            "\nAdvanced Sorting\n"
                            "1. Battery Level\n"
                            "2. Rental Price\n"
                            "3. Back\n"
                            "Enter choice: "
                        ))
                    except ValueError:
                        print("Enter a valid number.")
                        continue

                    if sort_choice == 1:
                        fleet.sort_fleet("battery", hub_name)
                        break
                    elif sort_choice == 2:
                        fleet.sort_fleet("price", hub_name)
                        break
                    elif sort_choice == 3:
                        break
                    else:
                        print("Invalid Choice.")

            elif choice == 9 :
                break

            else :
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
