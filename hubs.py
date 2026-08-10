from vehicle import Vehicle


class Hub:
    def __init__(self, hub_name):
        self.__hub_name = hub_name
        self.__vehicles = []

    def get_hub_name(self):
        return self.__hub_name

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            print("Only Vehicle objects can be added.")
            return False

        duplicate = [v for v in self.__vehicles if v == vehicle]
        if duplicate:
            print("Vehicle Id already exits in hub")
            return False

        self.__vehicles.append(vehicle)
        print("Vehicle Added Successfully.")
        return True

    def remove_vehicle(self, vehicle_id):
        if len(self.__vehicles) == 0:
            print("No vehicle found")
            return None

        for vehicle in self.__vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                self.__vehicles.remove(vehicle)
                print("Vehicle Removed Successfully.")
                return vehicle

        print("Vehicle not found")
        return None

    def get_vehicles(self):
        return self.__vehicles

    def __str__(self):
        return f"Hub : {self.__hub_name}"
