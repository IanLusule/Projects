import os
from datetime import datetime

def collect_recipe(file_name):
    print("Recipe Collector")
    print("Enter your recipes (type 'done' to finish):")

    with open(file_name, "a") as file:
        today = datetime.now().strftime("%d/%m/%Y")
        file.write(f"\n\nDate: {today}\n")
        
        while True:
            recipe = input("Recipe Name: ")
            if recipe.lower() == "done":
                break
            ingredients = input("Ingredients: ")
            instructions = input("Instructions: ")
            file.write(f"Recipe: {recipe}\nIngredients: {ingredients}\nInstructions: {instructions}\n\n")
    
    print(f"Your recipes have been saved to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recipe_collector.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    collect_recipe(file_name)

