from vehicle import Vehicle


class EcoRideMain:
    def __init__(self) -> None:
        pass
    def run(self) -> None:
        print("Welcome to Eco-Ride Urban Mobility System")

        car = Vehicle("001", "Scorpio S11", 30, "Good", 2500)
        print("Testing Vehicle details:")
        print(car)

        car.set_battery_percentage(80)
        car.set_rental_price(3000)
        print("\nAfter Update:")
        print(car)


if __name__ == "__main__":
    app = EcoRideMain()
    app.run()
