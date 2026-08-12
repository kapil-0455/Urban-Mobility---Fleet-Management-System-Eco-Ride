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


def test_invalid_battery():

    with pytest.raises(ValueError):
        ElectricCar("001", "Volvo", -100, "Available", 50000, 5)


def test_negative_rental_price():

    with pytest.raises(ValueError):
        ElectricCar("001", "Volvo", 100, "Available", -50000, 5)


def test_vehicle_equality():
    car1 = ElectricCar("001", "Volvo", 100, "Available", 50000, 5)
    car2 = ElectricCar("001", "Tesla", 80, "On Trip", 40000, 4)
    assert car1 == car2
