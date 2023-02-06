class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = input("How many Dollar Coins?: ")
        half_dollars = input("How many Half Dollars?: ")
        quarters = input("How many Quarters?: ")
        nickles = input("How many Nickles?: ")
        total = (float(dollars) * 1) + (float(half_dollars) * 0.5) + (float(quarters) * 0.25) + (float(nickles) * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost < coins:
            print("Insufficient funds, cancelling order.")
            return False
        change = round(cost - coins, 2)
        print("Thank you for purchasing! Here is your change: $", change)
        return True
