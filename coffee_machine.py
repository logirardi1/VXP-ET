class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.money = 0
        self.DISPENSER = 2000
        # ingredients in order: (water, milk, coffee)
        self.REQUIRED_RESOURCES_FOR_LATTE = {"water": 12, "milk": 100, "coffee": 30, "price": 2.1}
        self.REQUIRED_RESOURCES_FOR_ESPRESSO = {"water": 80, "milk": 0, "coffee": 50, "price": 1.0}
        self.REQUIRED_RESOURCES_FOR_CAPPUCCINO = {"water": 32, "milk": 100, "coffee": 30, "price": 4.6}

    def pour_water(self, water_in_mls):
        if self.water + water_in_mls <= self.DISPENSER:
            self.water += water_in_mls
        return self.water

    def pour_milk(self, milk_in_mls):
        if self.milk + milk_in_mls <= self.DISPENSER:
            self.milk += milk_in_mls
        return self.milk

    def pour_coffee(self, coffee_in_grams):
        if self.coffee + coffee_in_grams <= self.DISPENSER:
            self.coffee += coffee_in_grams
        return self.coffee

    def insert_coin(self, penny, nickel, dime, quarter):
        if penny < 0 or nickel < 0 or dime < 0 or quarter < 0:
            print("You can't withdraw money from the machine!")
            return False
        self.money += penny * 0.1
        self.money += nickel * 0.5
        self.money += dime * 0.10
        self.money += quarter * 0.25
        return True

    def print_report(self):
        print("Water: " + str(self.water) + "ml")
        print("Milk: " + str(self.milk) + "ml")
        print("Coffe: " + str(self.coffee) + "g")
        print("Money: " + "$" + str(self.money))

    def _withdraw_resources(self, coffee_type):
        if coffee_type == "cappuccino":
            coffee_ready = self._withdraw_resources_for_cappuccino()
            return coffee_ready
        elif coffee_type == "latte":
            coffee_ready = self._withdraw_resources_for_latte()
            return coffee_ready
        elif coffee_type == "espresso":
            coffee_ready = self._withdraw_resources_for_espresso()
            return coffee_ready
        return False

    def _withdraw_resources_for_espresso(self):
        can_proceed = True
        # ingredients in order: (water, milk, coffee)
        if self.REQUIRED_RESOURCES_FOR_ESPRESSO["water"] > self.water:
            print("Error! please pour more water into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_ESPRESSO["milk"] > self.milk:
            print("Error! please pour more milk into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_ESPRESSO["coffee"] > self.coffee:
            print("Error! please pour more coffee into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_ESPRESSO["price"] > self.money:
            print("Error! Not enough money")
            can_proceed = False

        if can_proceed:
            self._withdraw_ingredients(self.REQUIRED_RESOURCES_FOR_ESPRESSO["water"],
                                       self.REQUIRED_RESOURCES_FOR_ESPRESSO["milk"],
                                       self.REQUIRED_RESOURCES_FOR_ESPRESSO["coffee"],
                                       self.REQUIRED_RESOURCES_FOR_ESPRESSO["price"])
            return True
        return False

    def _withdraw_resources_for_latte(self):
        can_proceed = True
        # ingredients in order: (water, milk, coffee)
        if self.REQUIRED_RESOURCES_FOR_LATTE["water"] > self.water:
            print("Error! please pour more water into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_LATTE["milk"] > self.milk:
            print("Error! please pour more milk into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_LATTE["coffee"] > self.coffee:
            print("Error! please pour more coffee into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_LATTE["price"] > self.money:
            print("Error! Not enough money")
            can_proceed = False

        if can_proceed:
            self._withdraw_ingredients( self.REQUIRED_RESOURCES_FOR_LATTE["water"],
                                        self.REQUIRED_RESOURCES_FOR_LATTE["milk"],
                                        self.REQUIRED_RESOURCES_FOR_LATTE["coffee"],
                                        self.REQUIRED_RESOURCES_FOR_LATTE["price"])
            return True
        return False

    def _withdraw_resources_for_cappuccino(self):
        can_proceed = True
        # ingredients in order: (water, milk, coffee)
        if self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["water"] > self.water:
            print("Error! please pour more water into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["milk"] > self.milk:
            print("Error! please pour more milk into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["coffee"] > self.coffee:
            print("Error! please pour more coffee into the machine.")
            can_proceed = False
        if self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["price"] > self.money:
            print("Error! Not enough money")
            can_proceed = False

        if can_proceed:
            self._withdraw_ingredients( self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["water"],
                                        self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["milk"],
                                        self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["coffee"],
                                        self.REQUIRED_RESOURCES_FOR_CAPPUCCINO["price"])
            return True
        return False

    def _withdraw_ingredients(self, water, milk, coffee, price):
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.money -= price
        return True

    def turn_on(self):
        on = True
        while on:
            opcao = input("What would you like (espresso/latte/cappuccino/report): ").lower().strip()
            if opcao == "off":
                break
            if opcao == "report":
                self.print_report()
                continue
            print("Please Insert Coins: ")
            pennies = int(input("How many pennies: "))
            nickels = int(input("How many nickels: "))
            dimes = int(input("How many dimes: "))
            quarters = int(input("How many quarters: "))
            self.insert_coin(pennies, nickels, dimes, quarters)

            if self._withdraw_resources(opcao):
                print("Here is your {} ☕. Enjoy!".format(opcao))
            else:
                print("Sorry, your request was not possible.")


if __name__ == '__main__':
    machine = CoffeeMachine()
    machine.turn_on()
    