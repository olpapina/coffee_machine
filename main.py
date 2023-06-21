import sys

clients = list(client for client in range(100))
type_of_drinks = []
espresso = (100, 0, 10, 2.5)
latte = (150, 150, 15, 3.5)
cappuccino = (180, 50, 15, 3.0)
resources = {"water_volume": 2000, "milk_volume": 500, "coffee_volume": 1000, "money_balance": 0.0}


def answer_client():
    while True:
        type_of_drink = input(
            "What would you like? (espresso/latte/cappuccino) or print 'OFF' to finish working:").lower().strip()
        if type_of_drink in ["espresso", "latte", "cappuccino", "off"]:
            if type_of_drink == "off":
                turn_off_machine()
            return type_of_drink
        else:
            continue


def count_resources(cups):
    global resources
    if cups[0] > resources["water_volume"] or \
            cups[1] > resources["milk_volume"] or cups[2] > resources["coffee_volume"]:
        if cups[0] > resources["water_volume"]:
            print("Sorry there is not enough water")
        if cups[1] > resources["milk_volume"]:
            print("Sorry there is not enough milk")
        if cups[2] > resources["coffee_volume"]:
            print("Sorry there is not enough coffee")
        return 0
    else:
        resources["water_volume"] -= cups[0]
        resources["milk_volume"] -= cups[1]
        resources["coffee_volume"] -= cups[2]
        return 1


def turn_off_machine():
    print("The coffee machine is turned off. See you later")
    sys.exit()


def print_report():
    global resources
    print(f'Water: {resources["water_volume"]} ml')
    print(f'Milk: {resources["milk_volume"]} ml')
    print(f'Coffee: {resources["coffee_volume"]} g')
    print(f'Money: {resources["money_balance"]} $')


def count_money(cost):
    print(f'It costs {cost} $')
    client_coins = input("Enter the money: coins  2, 1, 0.5, 0.25, 0.10, 0.05, 0.01 >>")
    coins = client_coins.split()
    client_sum = 0.0
    for coin in coins:
        client_sum += float(coin)
    if client_sum == cost:
        return client_sum
    if client_sum < cost:
        print("Don't enough money")
        return 0
    if client_sum > cost:
        change = client_sum - cost
        print(f"Here is {change} dollars in change.")
        return cost


def check_money(type_drink):
    count = count_resources(type_drink)
    if count:
        client_money = count_money(type_drink[3])
        if client_money > 0:
            return [client_money, count]
    return [0, 0]


for client in clients:
    type_of_drinks.append(answer_client())
    flags = []
    print_report()
    if type_of_drinks[client] == "espresso":
        flags = check_money(espresso)
    if type_of_drinks[client] == "latte":
        flags = check_money(latte)
    if type_of_drinks[client] == "cappuccino":
        flags = check_money(cappuccino)
    if flags[1] == 1:
        resources["money_balance"] += flags[0]
        if flags[0]:
            print_report()
    else:
        print("Please, check the resources")
    print("Next client, please")
