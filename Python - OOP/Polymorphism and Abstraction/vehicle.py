from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self,fuel_quantity,fuel_consumption):

        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self,  distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    AIR_CONDITIONER = 0.9

    def drive(self,distance):

        fuel = (self.AIR_CONDITIONER + self.fuel_consumption) * distance

        if fuel <= self.fuel_quantity:
            self.fuel_quantity -= fuel

    def refuel(self, fuel):

        self.fuel_quantity += fuel


class Truck(Vehicle):

    AIR_CONDITIONER = 1.6

    def drive(self, distance):

        fuel = (self.AIR_CONDITIONER + self.fuel_consumption) * distance

        if fuel <= self.fuel_quantity:
            self.fuel_quantity -= fuel

    def refuel(self, fuel):

        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
