"""
Author: Eugenia Tate 
Date: August 31, 2025 

eugeniatate.py 
"""
import requests 
import json 
import pandas as pd

def get_random_cocktails(n):
    """
    This method calls CocktailDB API via GET n number of times and parses the JSON data to 
    collect data about each cocktail such as cocktail names, ingredients and their measurements 
    as well as instructions. 

    Parameters: 
     n - number of cocktails to fetch 

    Returns: 
    df - pandas DataFrame containing cocktail information 
    """
    recipes = []        # list to hold cocktail recipe dictionaries 
    # for number n of cocktails to retrieve, make API call and extract information needed 
    for i in range(n):
        url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
        response = requests.get(url).json()
        drink = response["drinks"][0]       # retrieve first cocktail from the drinks list 

        # Collect ingredients + measures
        ingredients = []
        for i in range(1, 16):  # any cocktail may only have up to 15 possible ingredients
            ingredient = drink.get(f"strIngredient{i}")
            measure = drink.get(f"strMeasure{i}")
            if ingredient and ingredient.strip() != "":     # if cocktail has ingredients
                # if measure is not null, append it together with ingredient
                if measure:
                    ingredients.append(f"{measure.strip()} {ingredient.strip()}")
                # measure is null, append just the ingredient 
                else:
                    ingredients.append(ingredient.strip())
        # add a new cocktail dictionary to the list
        recipes.append({
            "name": drink["strDrink"],
            "instructions": drink["strInstructions"],
            "ingredients": ingredients
        })
        # convert list of cocktail dictionaries into a DataFrame (each row is a cocktail)
        df = pd.DataFrame(recipes)

    return df

if __name__ == "__main__":
    # Get 5 random cocktails formatted in a recipe format 
    df = get_random_cocktails(5)
    print("5 Random Cocktail Recipes:")
    for i, row in df.iterrows():
        print(f"\n{row['name']}")
        print("Ingredients:")
        for ingredient in row['ingredients']:
            print(f"  - {ingredient}")
        print("Instructions:", row['instructions'])

# Notes:
# This dataset contains randomly selected cocktail recipes, including their names, ingredients with measurements,
# and preparation instructions. 
# This script's purpose is beaing a fun recipe recommendation tool. 
# If you don't like first 5 randomly selected cocktail recipes, you can re-run and check out the next 5. 