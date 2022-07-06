from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    items_dict = {
        "espresso": [50, 0, 18, 1.5],
        "latte": [200, 150, 24, 2.5],
        "cappuccino": [250, 50, 24, 3]
    }

    def report_prices():
        [print(f"{item} price: ${ingredients[-1]}") for item, ingredients in items_dict.items()]

    maker = CoffeeMaker()
    money = MoneyMachine()
    menu_list = Menu()
    machine_on = True
    while machine_on:
        choose = input(f"Write report for details!\nor What do you want to drink? {menu_list.get_items()}: ").lower()
        if choose == "off":
            machine_on = False
        elif choose == "report":
            (maker.report())
            (report_prices())
            (money.report())
        else:
            drink_ingredients = items_dict[choose]
            items = MenuItem(choose, drink_ingredients[0], drink_ingredients[1], drink_ingredients[2],
                             drink_ingredients[3])
            can_make = maker.is_resource_sufficient(items)
            if can_make:
                process_of_money = money.make_payment(items.cost)
                if process_of_money:
                    maker.make_coffee(items)


if __name__ == "__main__":
    coffee_machine()



