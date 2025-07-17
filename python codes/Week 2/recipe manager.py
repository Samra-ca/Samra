import json

# Load saved recipes
def load_recipes():
    try:
        with open("recipes.txt", "r") as f:
            return json.load(f)
    except:
        return {}

# Save recipes to file
def save_recipes(recipes):
    with open("recipes.txt", "w") as f:
        json.dump(recipes, f)

# Show all recipes
def show_recipes(recipes):
    if not recipes:
        print("No recipes found.")
    else:
        for name, ingredients in recipes.items():
            print(f"\n{name.title()}:")
            print(", ".join(ingredients))

# Main
recipes = load_recipes()

while True:
    print("\n1. Add Recipe\n2. View Recipes\n3. Search by Ingredient\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Recipe name: ").lower()
        ing = input("Ingredients (comma separated): ").split(",")
        recipes[name] = [i.strip() for i in ing]
        save_recipes(recipes)

    elif choice == "2":
        show_recipes(recipes)

    elif choice == "3":
        item = input("Search for ingredient: ").lower()
        found = False
        for name, ingredients in recipes.items():
            if item in [i.lower() for i in ingredients]:
                print(f"{name.title()} has {item}")
                found = True
        if not found:
            print("No recipe found with that ingredient.")

    elif choice == "4":
        break

    else:
        print("Invalid option.")