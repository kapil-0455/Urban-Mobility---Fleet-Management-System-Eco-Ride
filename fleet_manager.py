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
        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                hub.add_vehicle(vehicle)
                print("Vehicle Added Successfully.")
                return

        print("Hub not found.")

    def remove_vehicle_to_hub(self , hub_name , vehicle_id):
        hub_name = hub_name.strip()
        if hub_name == "":
            raise ValueError('Hub cannot be empty')

        for hub in self.__hubs:
            if hub.get_hub_name().lower() == hub_name.lower():
                hub.remove_vehicle(vehicle_id)
                print("Vehicle removed Successfully.")
                return
            
        print("Hub not found.")


    def display_hubs(self):
        for hub in self.__hubs:
            print(hub)
            for vehicle in hub.get_vehicles():
                print("   ", vehicle)