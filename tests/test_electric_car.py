import pytest

from electric_car import ElectricCar


@pytest.fixture
def car():

    return ElectricCar("001", "Volvo", 100, "Available", 50000, 5)


def test_vehicle_id(car):
    assert car.get_vehicle_id() == "001"


def test_model(car):
    assert car.get_model() == "Volvo"


def test_battery_percentage(car):
    assert car.get_battery_percentage() == 100


def test_maintenance_status(car):
    assert car.get_maintenance_status() == "Available"


def test_rental_price(car):
    assert car.get_rental_price() == 50000


def test_seating_capacity(car):
    assert car.get_seating_capacity() == 5


def test_calculate_trip_cost(car):
    result = car.calculate_trip_cost(10)
    assert result == 10.0


@pytest.mark.parametrize("invalid_battery", [-50, -1, 101, 200])
def test_invalid_battery_values(invalid_battery):
    with pytest.raises(ValueError):
        ElectricCar("001", "Volvo", invalid_battery, "Available", 50000, 5)


@pytest.mark.parametrize("distances", [-1, -20, -50])
def test_calculate_invalid_trip_cost(distances, car):
    with pytest.raises(ValueError):
        car.calculate_trip_cost(distances)


@pytest.mark.parametrize("invalid_seats", [30, 20, -8])
def test_invalid_seating_capacity(invalid_seats, car):
    with pytest.raises(ValueError):
        car.set_seating_capacity(invalid_seats)


def test_negative_rental_price():

    with pytest.raises(ValueError):
        ElectricCar("001", "Volvo", 100, "Available", -50000, 5)


def test_vehicle_equality():
    car1 = ElectricCar("001", "Volvo", 100, "Available", 50000, 5)
    car2 = ElectricCar("001", "Tesla", 80, "On Trip", 40000, 4)
    assert car1 == car2
