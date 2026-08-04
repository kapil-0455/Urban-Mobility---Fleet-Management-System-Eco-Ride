from vehicle import Vehicle


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)
        self.set_seating_capacity(seating_capacity)

    # Getter
    def get_seating_capacity(self):
        return self.__seating_capacity

    # Setter
    def set_seating_capacity(self, seating_capacity):
        if 1 <= seating_capacity <= 7:
            self.__seating_capacity = seating_capacity
        else:
            raise ValueError("Seating capacity must be between 1 and 7.")

    def __str__(self):
        return f"ElectricCar [ID: {self.get_vehicle_id()}, Model: {self.get_model()}, Battery: {self.get_battery_percentage()}%, Maintenance: {self.get_maintenance_status()}, Rental Price: {self.get_rental_price()}, Seating Capacity: {self.__seating_capacity}]"
