import json


def import_from_file(file_name):
    """ Method to add new cars in system from JSON file

    :param file_name:
    :return: None
    """
    to_add = []
    with open(file_name, "r") as json_file:
        cars = json.load(json_file)

        for car in cars["cars"]:
            print(car)

if __name__ == "__main__":
    import_from_file("cars.json")