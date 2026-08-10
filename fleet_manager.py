import csv
from collections import defaultdict

from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from hubs import Hub


class FleetManager:
    def __init__(self):
        self.__hubs = []
        self.__vehicle_categories = defaultdict(list)

    def add_hub(self, hub_name):

        hub_name = hub_name.strip()
        if hub_name == "":
            raise ValueError("Hub cannot be empty")

        # Check duplicate
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                print("Hub already exists.")
                return

        self.__hubs.append(Hub(hub_name))
        print("Hub Added Successfully.")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        hub_name = hub_name.strip()
        if hub_name == "":
            raise ValueError("Hub cannot be empty.")
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                added = hub.add_vehicle(vehicle)

                if added:
                    if isinstance(vehicle, ElectricCar):
                        self.__vehicle_categories["Electric Car"].append(vehicle)
                    elif isinstance(vehicle, ElectricScooter):
                        self.__vehicle_categories["Electric Scooter"].append(vehicle)

                return

        print("Hub not found.")

    def remove_vehicle_to_hub(self, hub_name, vehicle_id):
        hub_name = hub_name.strip()

        if hub_name == "":
            raise ValueError("Hub cannot be empty")

        vehicle_id = vehicle_id.strip()

        if vehicle_id == "":
            raise ValueError("Vehicle ID cannot be empty.")

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                removed_vehicle = hub.remove_vehicle(vehicle_id)
                if removed_vehicle:
                    if isinstance(removed_vehicle, ElectricCar):
                        self.__vehicle_categories["Electric Car"].remove(
                            removed_vehicle
                        )

                    elif isinstance(removed_vehicle, ElectricScooter):
                        self.__vehicle_categories["Electric Scooter"].remove(
                            removed_vehicle
                        )
                return

        print("Hub not found.")

    def display_hubs(self):
        if len(self.__hubs) == 0:
            print("No hubs available")
            return
        for hub in self.__hubs:
            print(hub)
            for vehicle in hub.get_vehicles():
                print("   ", vehicle)

    def search_by_hub(self, hub_name):
        hub_name = hub_name.strip().lower()
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name:
                print(f"Vehicle in Hub : {hub.get_hub_name()}")
                if len(hub.get_vehicles()) == 0:
                    print("No vehicle in this hub")
                else:
                    for vehicle in hub.get_vehicles():
                        print(vehicle)
                return

        print("Hub not found.")

    def search_by_battery(self):
        vehicles = []
        for hub in self.__hubs:
            vehicles.extend(hub.get_vehicles())

        high_battery_vehicles = list(
            filter(lambda vehicle: vehicle.get_battery_percentage() > 80, vehicles)
        )

        if len(high_battery_vehicles) == 0:
            print("No vehicle has battery greater than 80%.")
            return

        print("High Battery Vehicles (>80%):")
        for vehicle in high_battery_vehicles:
            print(vehicle)

    def categorized_view(self):
        if len(self.__vehicle_categories) == 0:
            print("No vehicles available.")
            return

        for vehicle_type, vehicles in self.__vehicle_categories.items():
            if len(vehicles) == 0:
                continue

            print(f"\n {vehicle_type}")

            for vehicle in vehicles:
                print(f"{vehicle}")

    def fleet_analytics(self):
        status_dict = {"Available": 0, "On Trip": 0, "Under Maintenance": 0}
        for hub in self.__hubs:
            for vehicle in hub.get_vehicles():
                status = vehicle.get_maintenance_status()
                status_dict[status] = status_dict.get(status, 0) + 1

        print("\n==========Fleet Analytics==============\n")
        for vehicle, vehicle_count in status_dict.items():
            print(f"{vehicle} : {vehicle_count}\n")

    def alphabet_sort(self, hub_name):
        hub_name = hub_name.strip()
        if hub_name == "":
            print("Hub cannot be empty")
            return

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                vehicles = hub.get_vehicles()

                if len(vehicles) == 0:
                    print("No vehicles in this hub")
                    return

                sorted_vehicles = sorted(
                    vehicles, key=lambda vehicle: vehicle.get_model().lower()
                )
                print("vehicle orderd alphabeticaly")

                for vehicle in sorted_vehicles:
                    print(vehicle)

                return

        print("Hub not Found")

    def sort_fleet(self, sort_type, hub_name):

        hub_name = hub_name.strip()
        if hub_name == "":
            print("Hub cannot be empty")
            return

        sort_type = sort_type.strip().lower()

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                vehicles = hub.get_vehicles()

                if len(vehicles) == 0:
                    print("No vehicles available in this hub")
                    return

                if sort_type == "battery":
                    sorted_vehicles = sorted(
                        vehicles,
                        key=lambda vehicle: vehicle.get_battery_percentage(),
                        reverse=True,
                    )
                    print(f"\nVehicles in {hub.get_hub_name()} sorted by Battery\n")

                elif sort_type == "price":
                    sorted_vehicles = sorted(
                        vehicles, key=lambda vehicle: vehicle.get_rental_price()
                    )
                    print(
                        f"\nVehicles in {hub.get_hub_name()} sorted by Rental Price\n"
                    )

                else:
                    print("Invalid option type")
                    return

                for vehicle in sorted_vehicles:
                    print(vehicle)

                return

        print("Hub not found")

    def save_to_csv(self, filename):
        with open(filename, "w") as f:
            writer = csv.writer(f)

            writer.writerow(
                [
                    "hub_name",
                    "vehicle_type",
                    "vehicle_id",
                    "model",
                    "battery",
                    "maintenance",
                    "rental_price",
                    "seating_capacity",
                    "max_speed",
                ]
            )

            for hub in self.__hubs:
                for vehicle in hub.get_vehicles():
                    if isinstance(vehicle, ElectricCar):
                        writer.writerow(
                            [
                                hub.get_hub_name(),
                                "Electric Car",
                                vehicle.get_vehicle_id(),
                                vehicle.get_model(),
                                vehicle.get_battery_percentage(),
                                vehicle.get_maintenance_status(),
                                vehicle.get_rental_price(),
                                vehicle.get_seating_capacity(),
                                None
                            ]
                        )

                    elif isinstance(vehicle, ElectricScooter):
                        writer.writerow(
                            [
                                hub.get_hub_name(),
                                "Electric Scooter",
                                vehicle.get_vehicle_id(),
                                vehicle.get_model(),
                                vehicle.get_battery_percentage(),
                                vehicle.get_maintenance_status(),
                                vehicle.get_rental_price(),
                                None,
                                vehicle.get_max_speed_limit()
                            ]
                        )

        print("Fleet data saved successfully.")

    def load_from_csv(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    hub_name = row["hub_name"]
                    hub_exists = False

                    for hub in self.__hubs:
                        if hub.get_hub_name().lower() == hub_name.lower():
                            hub_exists = True
                            break

                    if not hub_exists:
                        self.add_hub(hub_name)
                    
                    vehicle_id = row["vehicle_id"]
                    model = row["model"]
                    battery = int(row["battery"])
                    maintenance = row["maintenance"]
                    rental_price = float(row["rental_price"])

                    if row["vehicle_type"] == "Electric Car":
                        seating_capacity = int(row["seating_capacity"])
                        vehicle = ElectricCar(
                            vehicle_id,
                            model,
                            battery,
                            maintenance,
                            rental_price,
                            seating_capacity
                        )

                    elif row["vehicle_type"] == "Electric Scooter":
                        max_speed = int(row["max_speed"])

                        vehicle = ElectricScooter(
                            vehicle_id,
                            model,
                            battery,
                            maintenance,
                            rental_price,
                            max_speed
                        )
                    else:
                        print("Invalid vehicle type in CSV.")
                        continue
                    self.add_vehicle_to_hub(hub_name, vehicle)
            print("Fleet data loaded successfully.")

        except FileNotFoundError:
            print("No saved fleet data found.")
