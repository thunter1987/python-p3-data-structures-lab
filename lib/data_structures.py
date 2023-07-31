spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    foods = []
    for food in spicy_foods:
        foods.append(food["name"])

    return foods


def get_spiciest_foods(spicy_foods):
    foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            foods.append(food)
    return foods
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = food["heat_level"] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    heat_levels = 0
    for food in spicy_foods:
        heat_levels += int(food["heat_level"])
        average = heat_levels / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

