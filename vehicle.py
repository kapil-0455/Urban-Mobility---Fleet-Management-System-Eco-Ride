class Vehicle:
    def __init__(self, vehicle_id: str, model: str, battery_percentage: float):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage

    def __str__(self):
        return f"Vehicle [ID: {self.vehicle_id}, Model: {self.model}, Battery: {self.battery_percentage}%]"

if __name__ == '__main__':
    car = Vehicle('Scorpio' , 'S11' , '100')
    print(car)
