from enum import Enum

TypeOfCar = Enum('TypeOfCar', ['LIMOUSINE', 'CARAVAN', 'CABRIO'])

class Car:
    """
    Class represents a car with brand, model, type, manufacture year and price attributes,
    offering methods to manage and compare cars speeds.

    Functionality:
        - Tracks the total number of cars created and stores all instances.
        - Supports validation of car attributes and output functionalities.
    """

    def __init__(self, brand: str, model: str, type: str, year: int, price: float):
        """Initialize car

        :param brand: Car brand
        :param model: Car model
        :param type: Car type (Limousine, Caravan or Cabriolet)
        :param year: Manufacture year of car
        :param price: Car price
        :return:
        """
        self.brand = brand
        self.model = model
        self.type = type
        self.year = year
        self.price = price

    def __str__(self):
        """ String representation of the car in console display

        :return: String
        """
        return f"|Car: {self.brand} {self.model} {self.type} {self.year} = {self.price}|"
