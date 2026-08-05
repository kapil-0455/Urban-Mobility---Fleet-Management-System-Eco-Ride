from hubs import Hub


class FleetManager:

    def __init__(self):
        self.__hubs = []

    def add_hub(self, hub_name):

        hub_name = hub_name.strip()
        if hub_name == "":
            raise ValueError('Hub cannot be empty')
        
        # Check duplicate
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                print("Hub already exists.")
                return

        self.__hubs.append(Hub(hub_name))
        print("Hub Added Successfully.")
    
    def add_vehicle_to_hub(self, hub_name, vehicle):
        hub_name = hub_name.strip()
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                hub.add_vehicle(vehicle)
                return

        print("Hub not found.")

    def remove_vehicle_to_hub(self , hub_name , vehicle_id):
        hub_name = hub_name.strip()
        if hub_name == "":
            raise ValueError('Hub cannot be empty')

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                hub.remove_vehicle(vehicle_id)
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

    def search_by_hub(self , hub_name):
        hub_name = hub_name.strip().lower()
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name:
                print(f"Vehicle is in Hub : {hub.get_hub_name()}")
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

        high_battery_vehicles = list(filter(lambda vehicle : vehicle.get_battery_percentage() > 80 , vehicles))

        if len(high_battery_vehicles) == 0:
            print("No vehicle has battery greater than 80%.")
            return
    
        print("High Battery Vehicles (>80%):")
        for vehicle in high_battery_vehicles:
            print(vehicle)



