import pytest

from electric_car import ElectricCar
from hubs import Hub


@pytest.fixture
def hub():
    return Hub("Rajpura")


@pytest.fixture
def car():
    return ElectricCar("001", "Volvo", 100, "Available", 50000, 5)


def test_get_hub_name(hub):
    assert hub.get_hub_name() == "Rajpura"


def test_add_vehicles(hub, car):
    result = hub.add_vehicle(car)
    assert result == True


def test_duplicate_vehicle(hub, car):
    hub.add_vehicle(car)
    duplicate_car_id = ElectricCar("001", "BMW", 100, "On Trip", 500000, 2)

    result = hub.add_vehicle(duplicate_car_id)
    assert result == False


def test_remove_vehicle(hub, car):
    hub.add_vehicle(car)
    result = hub.remove_vehicle("001")
    assert result == car


def test_remove_non_existing_vehicle(hub, car):
    hub.add_vehicle(car)
    result = hub.remove_vehicle("002")
    assert result == None


def test_remove_from_empty_hub(hub):
    result = hub.remove_vehicle("001")
    assert result == None


def test_get_vehicles(hub, car):

    hub.add_vehicle(car)
    vehicles = hub.get_vehicles()

    assert len(vehicles) == 1
    assert vehicles[0] == car


def test_add_invalid_vehicle_type(hub):
    result = hub.add_vehicle(1234)

    assert result == False


def test_add_multiple_vehicles(hub, car):
    hub.add_vehicle(car)
    another_car = ElectricCar("002", "BMW", 100, "On Trip", 500000, 2)
    hub.add_vehicle(another_car)

    assert len(hub.get_vehicles()) == 2


def test_hub_string(hub):
    assert str(hub) == "Hub : Rajpura"
