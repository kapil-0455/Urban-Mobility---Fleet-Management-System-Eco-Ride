from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.set_battery_percentage(battery_percentage)
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    # Setters
    def set_battery_percentage(self, percentage):
        if 0 <= percentage <= 100:
            self.__battery_percentage = percentage
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative.")

    def __str__(self):
        return f"Vehicle [ID: {self.__vehicle_id}, Model: {self.__model}, Battery: {self.__battery_percentage}%, Maintenance: {self.__maintenance_status}, Rental Price: {self.__rental_price}]"

    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass
