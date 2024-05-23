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
    names = []
    for food in spicy_foods:
        if 'name' in food:
            names.append(food['name'])
    return names        
    pass

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if 'heat_level' in food and food['heat_level'] > 5:
            spiciest.append(food)
    return spiciest

    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if 'cuisine' in food and food['cuisine'] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods=get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    pass


def get_average_heat_level(spicy_foods):
    total_heat=sum(food["heat_level"] for food in spicy_foods)
    num_foods=len(spicy_foods)
    if num_foods == 0:
        return 0
    else: 
        return total_heat // num_foods
    pass

def create_spicy_food(spicy_foods, new_spicy_food):
   spicy_foods.append(new_spicy_food)
   return spicy_foods

