import pytest

from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from fleet_manager import FleetManager


@pytest.fixture
def fleet():
    return FleetManager()


@pytest.fixture
def car():
    return ElectricCar("001", "Volvo", 100, "Available", 50000, 5)


@pytest.fixture
def scooter():
    return ElectricScooter("002", "ola", 85, "On Trip", 500, 90)


def test_add_hub_success(fleet):
    fleet.add_hub("Rajpura")
    assert fleet.hub_exists("Rajpura") is True
    assert fleet.hub_exists("rajpura") is True


def test_add_empty_hub(fleet):
    with pytest.raises(ValueError):
        fleet.add_hub("")


def test_add_duplicate_hub(fleet):
    fleet.add_hub("Delhi")
    fleet.add_hub("delhi")
    assert len(fleet.get_hubs()) == 1


def test_hub_not_exists(fleet):
    assert fleet.hub_exists("Mumbai") is False


def test_add_vehicle_to_hub(fleet, car):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)

    hub = fleet.get_hubs()[0]
    assert len(hub.get_vehicles()) == 1
    assert hub.get_vehicles()[0] is car


def test_add_vehicle_to_empty_hub(fleet, car):
    with pytest.raises(ValueError):
        fleet.add_vehicle_to_hub("", car)


def test_add_vehicle_to_non_existent_hub(fleet, car, capsys):
    fleet.add_vehicle_to_hub("NonExistentHub", car)
    captured = capsys.readouterr()
    assert "Hub not found." in captured.out


def test_remove_vehicle_from_hub(fleet, car):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)

    fleet.remove_vehicle_to_hub("Rajpura", "001")
    hub = fleet.get_hubs()[0]
    assert len(hub.get_vehicles()) == 0


def test_remove_vehicle_empty_hub_name(fleet):
    with pytest.raises(ValueError):
        fleet.remove_vehicle_to_hub("", "001")


def test_remove_vehicle_empty_id(fleet):
    with pytest.raises(ValueError):
        fleet.remove_vehicle_to_hub("Delhi", "")


def test_remove_vehicle_from_non_existent_hub(fleet, capsys):
    fleet.remove_vehicle_to_hub("NonExistentHub", "001")
    captured = capsys.readouterr()
    assert "Hub not found." in captured.out


def test_search_by_hub(fleet, car, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)

    fleet.search_by_hub("Rajpura")
    captured = capsys.readouterr()
    assert "Vehicle in Hub : Rajpura" in captured.out
    assert "Volvo" in captured.out


def test_search_by_battery(fleet, car, scooter, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.search_by_battery()
    captured = capsys.readouterr()
    assert "High Battery Vehicles (>80%):" in captured.out
    assert "Volvo" in captured.out
    assert "ola" in captured.out


def test_fleet_analytics(fleet, car, scooter, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.fleet_analytics()
    captured = capsys.readouterr()
    assert "Available : 1" in captured.out
    assert "On Trip : 1" in captured.out


def test_alphabetical_sort(fleet, car, capsys):
    fleet.add_hub("Rajpura")
    car2 = ElectricCar("002", "BMW", 50, "Available", 5000, 4)

    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", car2)

    fleet.alphabet_sort("Rajpura")
    captured = capsys.readouterr()
    assert "vehicle orderd alphabeticaly" in captured.out
    assert captured.out.index("BMW") < captured.out.index("Volvo")


def test_alphabet_sort_empty_hub(fleet, capsys):
    fleet.add_hub("Rajpura")
    fleet.alphabet_sort("Rajpura")
    captured = capsys.readouterr()
    assert "No vehicles in this hub" in captured.out


def test_sort_by_battery(fleet, car, scooter, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.sort_fleet("battery", "Rajpura")
    captured = capsys.readouterr()
    assert "sorted by Battery" in captured.out

    assert captured.out.index("Volvo") < captured.out.index("ola")


def test_sort_by_price(fleet, car, scooter, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.sort_fleet("price", "Rajpura")
    captured = capsys.readouterr()
    assert "sorted by Rental Price" in captured.out

    assert captured.out.index("ola") < captured.out.index("Volvo")


def test_sort_fleet_invalid_and_empty(fleet, capsys):
    fleet.add_hub("Rajpura")

    fleet.sort_fleet("battery", "Rajpura")
    captured = capsys.readouterr()
    assert "No vehicles available in this hub" in captured.out

    car_temp = ElectricCar("001", "Tesla", 80, "Available", 1000, 4)
    fleet.add_vehicle_to_hub("Rajpura", car_temp)
    fleet.sort_fleet("invalid_type", "Rajpura")
    captured = capsys.readouterr()
    assert "Invalid option type" in captured.out


def test_categorized_view(fleet, car, scooter, capsys):
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.categorized_view()
    captured = capsys.readouterr()
    assert "Electric Car" in captured.out
    assert "Electric Scooter" in captured.out


def test_csv_save_and_load(fleet, car, scooter, tmp_path):
    file = tmp_path or "fleet.csv"

    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)

    fleet.save_to_csv(str(file))
    assert file.exists()

    new_fleet = FleetManager()
    new_fleet.load_from_csv(str(file))
    assert new_fleet.hub_exists("Rajpura") is True


def test_json_save_and_load(fleet, car, scooter, tmp_path):
    file = tmp_path or "fleet.json"
    fleet.add_hub("Rajpura")
    fleet.add_vehicle_to_hub("Rajpura", car)
    fleet.add_vehicle_to_hub("Rajpura", scooter)
    fleet.save_to_json(str(file))
    assert file.exists()
    new_fleet = FleetManager()
    new_fleet.load_from_json(str(file))
    assert new_fleet.hub_exists("Rajpura") is True


def test_csv_file_not_found(fleet, capsys):
    fleet.load_from_csv("abc.csv")
    captured = capsys.readouterr()
    assert "No saved fleet data found." in captured.out


def test_json_file_not_found(fleet, capsys):
    fleet.load_from_json("abc.json")
    captured = capsys.readouterr()
    assert "file Not found" in captured.out
