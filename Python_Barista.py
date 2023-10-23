# Python_Barista.py
# Author: Spencer Thomson
# Date: 10/23/2023
# Description: This is a modified version of the NetworkChuck Python Barista.
#              The script simulates a coffee ordering experience at a coffee shop.
#              It includes basic error handling and user interactions. This version
#              has additional features such as a dynamic menu and millionaire check.

import time  # For sleep function to simulate waiting time
import sys  # For system-level operations like exit
import os  # For clearing the console screen

def clear_screen():
    os.system('clear||cls')

def display_menu(items):
    for index, (item, price) in enumerate(items.items(), 1):
        print(f"{index}: {item} | ${price}")

clear_screen()
print("Hi, welcome to Breckenridge Coffee!!!!!")
name = input("What is your name?: ")
clear_screen()
millionaire_status = input(f"Hi {name}, are you a millionaire? (yes/no): ")
if millionaire_status.lower() != 'yes':
    print("Leave Breckenridge, poor person!")
    sys.exit(0)

clear_screen()
price1 = 3.00
price2 = 9.00
price3 = 8.25
price4 = 10.50

menu_items = {
    "Black Coffee": price1,
    "Caramel Mocha": price2,
    "Espresso": price3,
    "Latte Mocha": price4
}

print(f"Welcome {name}! Please choose from our menu below what you would like!")
display_menu(menu_items)

while True:
    option = input("Option: ")
    amount = input("How many?: ")

    try:
        option = int(option)
        amount = int(amount)
    except Exception as e:
        print(f"Oops! The value(s) you gave me was not a number/Integer.\nError: {e}")
        quit()

    if option > len(menu_items) or option <= 0:
        clear_screen()
        print(f"Sorry, we don't have an item for that number/option. Please pick again!")
        display_menu(menu_items)
        continue
    
    selected_item = list(menu_items.keys())[option - 1]
    selected_price = menu_items[selected_item]
    
    if amount <= 0:
        clear_screen()
        print(f'Sorry, but you need to order something from the menu. Please pick again!')
        display_menu(menu_items)
        continue
    
    clear_screen()
    print(f"Thank you for ordering {amount} {selected_item}(s). Your order will be done shortly!")
    break

total_wait_time = 60
apology_interval = 10

for _ in range(total_wait_time // apology_interval):
    print("Sorry for the wait...")
    for remaining in range(apology_interval, 0, -1):
        sys.stdout.write(f"\r[{remaining:2d}] seconds remaining until your order is ready.")
        sys.stdout.flush()
        time.sleep(1)
    clear_screen()

total_cost = round(amount * selected_price * 1.2, 2)
print(f"{name}! Your {amount} {selected_item}(s) is ready! Your total is: ${total_cost}\nPlease come and pick up your order, thank you for the tip.")
