import cashier
import data
import sandwich_maker


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
cashier_instance = cashier.Cashier


def main():
    """write the rest of the codes"""
    running = True
    while running:
        sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
        if sandwich_maker_instance.check_resources(recipes[sandwich_maker_instance.sandwich_size]):
            money_input = cashier_instance.process_coins(cashier_instance)
            if cashier_instance.transaction_result(cashier, recipes[sandwich_maker_instance.sandwich_size]["cost"], money_input):
                sandwich_maker_instance.make_sandwich(recipes[sandwich_maker_instance.sandwich_size], resources)
        for x in resources.values():
            if x == 0:
                running = False
    print("Closing, need to restock.")


if __name__ == "__main__":
    main()

