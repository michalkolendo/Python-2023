import csv
import psycopg2

connect_string = "dbname=my_database user=my_user password=secret host=127.0.0.1"

class FoodItem:
    def __init__(self, food_id, name, price):
        self.food_id = food_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"FoodItem({self.food_id},{self.name},{self.price})"


def load_food_items_from_csv(file_path):
    food_items = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = True

        for row in csv_reader:
            if header:
                header = False
                continue
            food_id, name, price = row
            food_item = FoodItem(food_id, name, price)
            food_items.append(food_item)

    return food_items


file_path = '..\\15_Pliki_tekstowe\\data\\foods.csv'
food_items_list = load_food_items_from_csv(file_path)


with psycopg2.connect(connect_string) as connection:
    cursor = connection.cursor()
    for food_item in food_items_list:
        statement = f"INSERT INTO fooditem(name, price) VALUES('{food_item.name}', {food_item.price});"
        print(statement)
        cursor.execute(statement)
    connection.commit()