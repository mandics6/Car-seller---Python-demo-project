from car import Car
import sys

class CarManager:
    """
    Class represents a car manager,
    offering methods for adding new car, remove car and searching car by some parameter.

    Functionality:
        - Tracks of all cars created and their count.
    """
    total_cars = 0
    cars = []

    @classmethod
    def get_cars(cls):
        """ Getter method for cars

        :return: List of cars
        """
        return cls.cars

    @classmethod
    def add_car(self, instance: Car):
        """ Method to add new car in system

        :param instance: Car that should be added
        :return: None
        """
        if isinstance(instance, Car):
            CarManager.total_cars += 1
            CarManager.cars.append(instance)
        else:
            print("*** Type of object that you tried to add is not type of Car! ***")

    @classmethod
    def remove_car(self, instance: Car):
        """ Method to remove car from system

        :param instance: Car that should be removed
        :return: None
        """
        if isinstance(instance, Car):
            CarManager.total_cars -= 1
            CarManager.cars.remove(instance)
        else:
            print("*** Type of object that you tried to add is not type of Car! ***")

    def search_by_price(self, min_price, max_price):
        """ Method for searching list of cars in price range [min_price, max_price]

        :param min_price: Minimum price for searching
        :param max_price: Maximum price for searching
        :return: List of searched cars
        """
        res = []
        for car in CarManager.cars:
            if car.price >= min_price and car.price <= max_price:
                res.append(car)
        return res

    def search_by_year(self, year):
        """ Method for searching list of cars by manufacture year in parameter, this is additional request. It could also be implemented in ascending year from this year

        :param year: Manufacture year of car
        :return: List of searched cars
        """
        res = []
        for car in CarManager.cars:
            if car.year == year:
                res.append(car)
        return res

    def search_by_type(self, type):
        """ Method for searching list of cars by type of car

        :param type: Type of car to search by
        :return: List of searched cars
        """
        res = []
        for car in CarManager.cars:
            if car.type == type:
                res.append(car)
        return res

    @classmethod
    def get_cars_list(cls):
        """ Method to print details of all cars created

        :return: List of cars
        """
        return cls.cars

