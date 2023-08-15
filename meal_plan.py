import csv
import random
from tabulate import tabulate

def get_meal_data():
    with open('meals.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        meal_data = []
        for row in reader:
            meal_data.append(row)
        meal_data.pop(0)
        for meal in meal_data:
            meal[2] = int(meal[2])
        return meal_data
    
def random_meal(meals):
    return meals.pop(random.randrange(len(meals)))
    
def generate_meal_plan(meals):
    meals = list(meals)
    nights_to_plan = 5
    selected_meals = []
    while nights_to_plan > 0:
        chosen_meal = random_meal(meals)
        if chosen_meal[2] > nights_to_plan:
            continue
        selected_meals.append(chosen_meal)
        nights_to_plan -= chosen_meal[2]
    return selected_meals

def print_meal(meal_plan, i):
    print(f"\nMeal Plan {i}")
    table = [["Meal", "Chef", "Nights"]]
    for meal in meal_plan:
        if meal[1] == "Both":
            meal[1] = random.choice(["Billy", "Nat"])
        table.append([meal[0],meal[1],meal[2]])
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        
meals = get_meal_data()
for i in range(4):
    meal_plan = generate_meal_plan(meals)
    print_meal(meal_plan, i+1)