from art import logo, logo2
from info import ingredients, price

print(logo)
print(logo2)

drink_order = True
#Function to process coins
def change(drink):
    quarters = float(input("Enter your quarters: ")) * .25  # n(.25)
    dimes = float(input("Enter your dimes: ")) * .10        # n(.10)
    nickels = float(input("Enter your nickels: ")) * .5     # n(.5)
    pennies = float(input("Enter your pennies: ")) * .1     # n(.1)
    total = quarters + dimes + nickels + pennies
    if total < price[drink]:
        return f'Sorry, not enough money. Here is your money back: ${round(total, 2)}.'
    else:
        if total > price[drink] or total == price[drink]:
            total -= price[drink]
            return f'Your total was: ${price[drink]}\nHere is your change: ${round(total,2)}, Enjoy your drink.'
#Drink functions
def espresso():
    if ingredients['milk'] < 50 or ingredients['coffee'] < 50:
        return False
    else:
        ingredients['milk'] -= 50
        ingredients['coffee'] -= 50

def latte():
    if ingredients['milk'] < 100 or ingredients['coffee'] < 50 or ingredients['water'] < 50:
        return False
    else:
        ingredients['milk'] -= 100
        ingredients['coffee'] -= 50
        ingredients['water'] -= 50

def cappuccino():
    if ingredients['milk'] < 100 or ingredients['coffee'] < 50 or ingredients['water'] < 10:
        return False
    else:
        ingredients['milk'] -= 100
        ingredients['coffee'] -= 50
        ingredients['water'] -= 10

def drink(option):
    if option == 'report':
        return ingredients
    elif option == 'espresso':
        return espresso()
    elif option == 'latte':
        return latte()
    elif option == 'cappuccino':
        return cappuccino()

while drink_order:
    choice = input("What would you like, Espresso/Latte/Cappuccino?\nEnter 'Report' for a list of ingredients & Prices. ").lower()
    if choice == 'report':
        print(f"Water: {ingredients['water']}ml, Milk: {ingredients['milk']}ml, Coffee: {ingredients['coffee']}m\nPrices: Espresso: ${price['espresso']}, Latte: ${price['latte']}, Cappuccino: ${price['cappuccino']}")
        should_continue = input("Would you like to order? 'Y' or 'N' ").lower()
        if should_continue == 'y':
            drink_order = True
        else:
            print("Thank you for stopping by.")
            drink_order = False
    else:
        # Check for the ingredients
        leftover = drink(choice)
        if leftover is False:
            print('Sorry Not enough Ingredients')
            drink_order = False
        # Check if user has enough money
        else:
            total_change = change(choice)
            print(total_change)




