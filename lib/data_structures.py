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
    names = [d["name"] for d in spicy_foods]
    return names
# returns a list of dictionaries where the heat level
#of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food.get("heat_level",  0) > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
   chili = "🌶"
   for food in spicy_foods:
       name = food["name"]
       cuisine = food["cuisine"]
       heat_level = food["heat_level"]
       heat_emoji = chili * heat_level
       print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
              

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
         if food.get("cuisine") == cuisine: 
          return food
 
def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_food)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    average_heat = total_heat_level / num_spicy_foods
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
