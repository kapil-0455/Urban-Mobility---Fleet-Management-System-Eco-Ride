from vehicle import Vehicle


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)
        self.set_max_speed_limit(max_speed_limit)

    # Getter
    def get_max_speed_limit(self):
        return self.__max_speed_limit

    # Setter
    def set_max_speed_limit(self, max_speed_limit):
        if 1<= max_speed_limit <=150:
            self.__max_speed_limit = max_speed_limit
        else:
            raise ValueError("Speed must be in this limit 1 - 150.")

    def __str__(self):
        return f"ElectricScooter [ID: {self.get_vehicle_id()}, Model: {self.get_model()}, Battery: {self.get_battery_percentage()}%, Maintenance: {self.get_maintenance_status()}, Rental Price: {self.get_rental_price()}, Max Speed Limit: {self.__max_speed_limit}]"


    # overriden function from vehicle class
    def calculate_trip_cost(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")
        return 1.00 + 0.15 * minutes
