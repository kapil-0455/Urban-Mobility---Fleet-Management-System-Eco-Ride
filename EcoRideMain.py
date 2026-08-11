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
                    "6. Fleet Analytics\n"
                    "7. Sort vehicle by Model in a Hub\n"
                    "8. Advanced Sorting (Battery/Price)\n"
                    "9. Load Data from CSV\n"
                    "10. Save Data in CSV\n"
                    "11. Load Data from JSON\n"
                    "12. Save Data in JSON\n"
                    "13. Exit\n"
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

                if not fleet.hub_exists(hub_name):
                    print("Hub not found.")
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
                hub_name = input("Enter Hub Name: ").strip()
                if not hub_name:
                    print("Hub name cannot be empty.")
                    continue
                if not fleet.hub_exists(hub_name):
                    print("Hub not found.")
                    continue
                vehicle_id = input("Enter Vehicle ID: ").strip()
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
                hub_name = input("Enter hub name: ").strip()
                if not hub_name:
                    print("Hub name cannot be empty.")
                    continue
                if not fleet.hub_exists(hub_name):
                    print("Hub not found.")
                    continue
                fleet.alphabet_sort(hub_name)
            
            elif choice == 8:
                hub_name = input("Enter Hub Name: ").strip()
                if not hub_name:
                    print("Hub name cannot be empty.")
                    continue
                if not fleet.hub_exists(hub_name):
                    print("Hub not found.")
                    continue
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

            elif choice == 9:
                filename = input("Enter CSV filename (default: fleet_data.csv): ").strip()
                if filename == "":
                    filename = "fleet_data.csv"
                print(f"\nLoading data from {filename}.")
                fleet.load_from_csv(filename)
                print("\n=== Current Fleet Data in System ===")
                fleet.display_hubs()

            elif choice == 10:
                filename = input("Enter CSV filename (default: fleet_data.csv): ").strip()
                if filename == "":
                    filename = "fleet_data.csv"
                fleet.save_to_csv(filename)
                print(f"Data saved successfully to {filename}.")

            elif choice == 11:
                filename = input("Enter JSON filename (default: fleet_data.json): ").strip()
                if filename == "":
                    filename = "fleet_data.json"
                print(f"\nLoading data from {filename}")
                fleet.load_from_json(filename)
                print("\n=== Current Fleet Data in System ===")
                fleet.display_hubs()

            elif choice == 12:
                filename = input("Enter JSON filename (default: fleet_data.json): ").strip()
                if filename == "":
                    filename = "fleet_data.json"
                fleet.save_to_json(filename)
                print(f"Data saved successfully to {filename}.")

            elif choice == 13:
                print("Thank you for using Eco-Ride Urban Mobility System!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
