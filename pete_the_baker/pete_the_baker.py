import math

def cakes(recipe, ingredients):
    ratio = []
    for i in recipe:
        if i not in ingredients:
            return 0
        if i in ingredients:
            ratio.append(ingredients[i]/recipe[i])
    return math.floor(sorted(ratio)[0])
