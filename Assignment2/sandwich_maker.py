import sys
import data

class SandwichMaker:
    sandwich_size = "small"

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.sandwich_size = input("What would you like to order today? (small/medium/large/off/report): ")
        while self.sandwich_size == "report":
            for x, y in data.resources.items():
                print(x, ": ", y)
            self.sandwich_size = input("What would you like to order today? (small/medium/large/off/report): ")
        if self.sandwich_size == "off":
            print("Closing Up")
            sys.exit()

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for x, y in ingredients["ingredients"].items():
            for z, w in data.resources.items():
                if x == z:
                    if y > w:
                        print("Insufficient", z, "cancelling order.")
                        return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for resource_name, resource_amt in order_ingredients.items():
            for ingredient_name, ingredient_amt, in sandwich_size["ingredients"].items():
                if resource_name == ingredient_name:
                    ingredient_value = ingredient_amt
                    current_value = resource_amt
                    total = current_value - ingredient_value
                    order_ingredients[resource_name] = total
