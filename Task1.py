from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for _ in range(ing_count):
            ingredients_temp = file.readline().split('|')
            ingredient_name = ingredients_temp[0].strip()
            quantity = ingredients_temp[1].strip()
            measure = ingredients_temp[2].strip()
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
pprint(cook_book, sort_dicts=False)
