import time

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24},
            "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0}
        }

resources = {"water": 300, "milk": 200, "coffee": 100}

coffee_machine_running = True
money = 0


def subtract_resources(coffe_name, coffee_ingredients):

    global resources

    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffe_name} ☕️ Enjoy!")
    print("")

    time.sleep(1)


def check_resources(coffee_ingredients):

    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"sorry, there's not enough {item} left. Come back later.")
            return False
    return True


def check_money(cost_of_coffee):

    global total_amount_paid
    global money

    if total_amount_paid > cost_of_coffee:
        change = round(total_amount_paid - cost_of_coffee, 2)
        print(f"Here is your ${change} in change.")
        print("")

        money += cost_of_coffee

        time.sleep(1)

        return True

    elif total_amount_paid == coffee_cost:
        money += cost_of_coffee

        time.sleep(1)

        return True

    else:
        print("Sorry, that's not enough money. Your coins have been refunded.")

        return False


while coffee_machine_running:

    coffee_type = input("""What would you like?
    'espresso' = $1.50
    'latte' = $2.50
    'cappuccino' = $3.00\n
type 'report' if you wish to see amount of ingredients left in machine
or type 'off' to turn off machine\n\n""").lower()

    if coffee_type == 'report':
        print("")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        print("")

        time.sleep(1)

    if coffee_type == 'off':
        coffee_machine_running = False

    if (coffee_type == 'espresso' or
            coffee_type == 'latte' or
            coffee_type == 'cappuccino'):

        order = MENU[coffee_type]

        if check_resources(order['ingredients']):

            print("")
            print('Please insert coins.')
            print("")
            num_quarters = int(input("How many quarters?: "))
            num_dimes = int(input("How many dimes?: "))
            num_nickels = int(input("How many nickels?: "))
            num_pennies = int(input("How many pennies?: "))
            print("")

            total_amount_paid = ((num_quarters * 0.25) + (num_dimes * 0.1) +
                                (num_nickels * 0.05) + (num_pennies * 0.01))


            if check_money(order['cost']):
                subtract_resources(coffee_type, order['ingredients'])
