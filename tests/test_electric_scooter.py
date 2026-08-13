import pytest

from electric_scooter import ElectricScooter


@pytest.fixture
def scooter():

    return ElectricScooter("001", "ola", 85, "Available", 500, 90)


def test_vehicle_id(scooter):
    assert scooter.get_vehicle_id() == "001"


def test_model(scooter):
    assert scooter.get_model() == "ola"


def test_battery_percentage(scooter):
    assert scooter.get_battery_percentage() == 85


def test_maintenance_status(scooter):
    assert scooter.get_maintenance_status() == "Available"


def test_max_speed_limit(scooter):
    assert scooter.get_max_speed_limit() == 90


def test_rental_price(scooter):
    assert scooter.get_rental_price() == 500


def test_calculate_trip_cost(scooter):
    result = scooter.calculate_trip_cost(10)
    assert result == 2.5


@pytest.mark.parametrize("distances", [-1, -10, -500])
def test_calculate_invalid_trip_cost(scooter, distances):
    with pytest.raises(ValueError):
        scooter.calculate_trip_cost(distances)


@pytest.mark.parametrize("max_speed", [-50, 900, 300])
def test_invalid_max_speed(scooter, max_speed):
    with pytest.raises(ValueError):
        scooter.set_max_speed_limit(max_speed)


@pytest.mark.parametrize("invalid_battery", [-50, 101, 200])
def test_invalid_battery_values(invalid_battery):
    with pytest.raises(ValueError):
        ElectricScooter("001", "ola", invalid_battery, "Available", 500, 90)


def test_negative_rental_price():
    with pytest.raises(ValueError):
        ElectricScooter("001", "ola", 85, "Available", -500, 90)
