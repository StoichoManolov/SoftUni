from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):

        self.users: List[User] = []
        self.vehicles: List[CargoVan, PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        driver = self.get_user(driving_license_number)

        if driver:
            return f"{driving_license_number} has already been registered to our platform."

        new_driver = User(first_name,last_name,driving_license_number)
        self.users.append(new_driver)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        number_plate = self.get_plate(license_plate_number)

        if vehicle_type not in self.VALID_VEHICLE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if number_plate:
            return f"{license_plate_number} belongs to another vehicle."

        plate = self.VALID_VEHICLE[vehicle_type](brand, model,license_plate_number)
        self.vehicles.append(plate)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        route = self.get_route(start_point, end_point, length)

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, route_id=len(self.routes) + 1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        driver = self.get_user(driving_license_number)
        vehicle = self.get_plate(license_plate_number)
        route = [r for r in self.routes if route_id == r.route_id][0]

        if driver.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            driver.decrease_rating()
        else:
            driver.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):

        damaged = [v for v in self.vehicles if v.is_damaged]

        sorted_damage = sorted(damaged, key=lambda v: (v.brand, v.model))
        count_damage = sorted_damage[:count]

        for v in count_damage:
            v.change_status()
            v.recharge()
        return f"{len(count_damage)} vehicles were successfully repaired!"

    def users_report(self):

        result = ['*** E-Drive-Rent ***']

        sorted_users = sorted(self.users, key=lambda k: -k.rating)
        [result.append(str(u)) for u in sorted_users]

        return '\n'.join(result)

    def get_user(self, driving_license_number: str):

        driver = [l for l in self.users if l.driving_license_number == driving_license_number]

        return driver[0] if driver else None

    def get_plate(self, license_plate_number):

        plate = [p for p in self.vehicles if p.license_plate_number == license_plate_number]
        return plate[0] if plate else None

    def get_route(self, start_point, end_point, length):

        route = [r for r in self.routes if start_point == r.start_point and
                 end_point == r.end_point]

        return route[0] if route else None





