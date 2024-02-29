from car import Car
import json
from datetime import date
from carManager import CarManager as cm
import csv
import aspose.pdf as ap

class User:
    """
    Class represents a user with saldo and manager??? ,
    offering various methods that support selling car, adding new car, etc.

    Functionality:
        - Tracks the transactions of all users.
    """
    transactions = []

    def __init__(self, name: str, saldo: float):
        """ Initialize user

        :param name: User's name
        :param saldo: User's saldo
        :param manager: Users CarManager that manage the cars
        :return: None
        """
        self.__name = name
        self.__saldo = saldo

    @property
    def saldo(self):
        """ Getter method for saldo

        :return: User's saldo
        """
        return self.__saldo

    def sell_car(self, car: Car, buyer: str):
        """ Method to sell car to buyer with name in parameter list ("buyer")

        :param car: Car to sell
        :param buyer:Buyer's name
        :return: None
        """
        today = date.today()
        cm.remove_car(car)
        self.__saldo += float(car.price)
        transaction = {"brand": car.brand, "model": car.model, "price": car.price, "buyer": buyer, "date": today.strftime("%d.%m.%y")}
        User.transactions.append(transaction)
        print("Car was sold successfully.")

    def add_new_car(self, brand, model, type, year, price):
        """ Method to make new car with parameters and add it to CarManager list

        :param brand: Car brand
        :param model: Car model
        :param type: Car type
        :param year: Car manufacture year
        :param price: Car price
        :return: None
        """
        if self.__saldo >= 1.2 * float(price):
            today = date.today()
            self.__saldo -= 1.2 * float(price)
            new_car = Car(brand, model, type, year, price)
            transaction = {"brand": new_car.brand, "model": new_car.model, "price": new_car.price, "buyer": self.__name, "date": today.strftime("%d.%m.%y")}
            User.transactions.append(transaction)
            cm.add_car(new_car)
            print("*** New car have been added successfully! ***")
        else:
            print("*** It is not possible to add a new car, due to lack of funds! ***")
            return

    def select_car_by_price(self, min_price, max_price):
        """ Method that return list of cars in price range

        :param min_price: Min price of car
        :param max_price: Max price of car
        :return: List of cars
        """
        res = []
        if min_price > max_price or max_price < 0 or min_price < 0:
            print("*** Not valid input! ***")
            exit(-1)
        for car in cm.get_cars():
            if float(car.price) >= min_price and float(car.price) <= max_price:
                res.append(car)

        for line in res:
            print(line)

        return res

    def select_car_by_year(self, year: int):
        """ Method that return list of cars produced in year

        :param year: Year of car
        :return: List of cars
        """
        res = []
        if year < 0:
            print("*** Not valid input! ***")
            exit(-1)
        for car in cm.get_cars():
            if int(car.year) == year:
                res.append(car)

        for line in res:
            print(line)

        return res

    def select_car_by_type(self, type: str):
        """ Method that return list of cars by type

        :param type: Type of car
        :return: List of cars
        """
        res = []
        if type != "Limousine" or type != "Caravan" or type != "Cabrio":
            print("*** Not valid input! ***")
            exit(-1)
        for car in cm.get_cars():
            if car.type == type:
                res.append(car)

        for line in res:
            print(line)

        return res

    def import_from_file(self, file_name):
        """ Method to add new cars in system from JSON file

        :param file_name:
        :return: None
        """
        with open(file_name, "r") as json_file:
            cars = json.load(json_file)

            for car in cars["cars"]:
                self.add_new_car(car["brand"], car["model"], car["type"], car["year"], car["price"])


    def generate_report(self):
        """ Method for generating report in PDF format

        :return: None
        """



    def save_transactions_to_csv_file(self, file_name):
        """ Method to save transactions in CSV file with mentioned name

        :param file_name: Name of output csv file that need to be generated
        :return: None
        """

        header = ["brand", "model", "price", "buyer", "date"]
        with open(file_name, "w") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)

            for transaction in User.transactions:
                csvwriter.writerow([transaction["brand"], transaction["model"], transaction["price"], transaction["buyer"], transaction["date"]])

    def select_car_from_list(self, list, brand: str, model: str, type: str, year: int, price: float):
        for car in list:
            if car["brand"] == brand:   # I don't have a clue why this doesn't work :/
                if car["model"] == model:
                    if car["type"] == type:
                        if car["year"] == year:
                            if car["price"] == price:
                                print("Do you want to sell it? (y/n)")
                                answer = input("Answer: ")
                                if answer == "y":
                                    buyer = input("Enter a buyer's name: ")
                                    self.sell_car(car, buyer)
                            else:
                                print("*** There is no car with these parameters! ***")
                        else:
                            print("*** There is no car with these parameters! ***")
                    else:
                        print("*** There is no car with these parameters! ***")
                else:
                    print("*** There is no car with these parameters! ***")
            else:
                print("*** There is no car with these parameters! ***")


print("Enter a parameters for new user (name, saldo): ")
name1 = input()
saldo1 = float(input())
user1 = User(name1, saldo1)

while(True):
    print("Operations:\n- Sell car (sell)\n- Add new car (add)\n- Select car by price (selectPrice)\n- Select car by year (selectYear)\n- Select car by type (selectType)\n- Import new cars from file (import)\n- Generate report (report)\n- Save transactions (save)\n- To QUIT enter \"exit\"")
    op = input("Enter your new operation to execute:")

    if op == "exit":
        exit(0)
    elif op == "sell":
        print("Enter a parameters for user's car (brand, model, type, year, price): ")
        brand1 = input()
        model1 = input()
        type1 = input("Limousine, Caravan, Cabrio: ")
        year1 = int(input())
        price1 = float(input())
        car1 = Car(brand1, model1, type1, year1, price1)

        buyer_name = input("Enter a name of buyer: ")
        user1.sell_car(car1, buyer_name)
    elif op == "add":
        print("Enter a parameters for user's car (brand, model, type, year, price): ")
        brand1 = input()
        model1 = input()
        type1 = input("Limousine, Caravan, Cabrio: ")
        year1 = input()
        price1 = input()
        user1.add_new_car(brand1, model1, type1, year1, price1)
    elif op == "selectPrice":
        print("Enter a price range for search: ")
        min_price = float(input("Min = "))
        max_price = float(input("Max = "))
        list = user1.select_car_by_price(min_price, max_price)

        print("Do you want to choose any car? (y/n)")
        answer = input("Answer: ")
        if answer == "y":
            print("Which car do you want to choose? (car parameters)")
            brand1 = input()
            model1 = input()
            type1 = input("Limousine, Caravan, Cabrio: ")
            year1 = int(input())
            price1 = float(input())

            user1.select_car_from_list(list, brand1, model1, type1, year1, price1)
        else:
            print("*** You didn't choose any car! ***\n")
    elif op == "selectYear":
        print("Enter a year for search: ")
        year = int(input("Year = "))
        list = user1.select_car_by_year(year)
        print("Do you want to choose any car? (y/n)")
        answer = input("Answer: ")
        if answer == "y":
            print("Which car do you want to choose? (car parameters)")
            brand1 = input()
            model1 = input()
            type1 = input("Limousine, Caravan, Cabrio: ")
            year1 = int(input())
            price1 = float(input())

            user1.select_car_from_list(list, brand1, model1, type1, year1, price1)
        else:
            print("*** You didn't choose any car! ***\n")
    elif op == "selectType":
        print("Enter a type for search: ")
        type = int(input("Type = "))
        list = user1.select_car_by_type(type)
        print("Do you want to choose any car? (y/n)")
        answer = input("Answer: ")
        if answer == "y":
            print("Which car do you want to choose? (car parameters)")
            brand1 = input()
            model1 = input()
            type1 = input("Limousine, Caravan, Cabrio: ")
            year1 = int(input())
            price1 = float(input())

            user1.select_car_from_list(list, brand1, model1, type1, year1, price1)
        else:
            print("*** You didn't choose any car! ***\n")
    elif op == "import":
        user1.import_from_file("cars.json")
        print("New cars have been added from JSON file")
    elif op == "report":
        # TODO make report in PDF
        None
    elif op == "save":
        user1.save_transactions_to_csv_file("transactions.csv")
        print("Transactions have been saved in CSV file")
    else:
        print("*** You didn't enter right operation! Please try again! ***\n")