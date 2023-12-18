import orders
import json
import requests
import sys

# Java Journeys Café Ordering System
# This program simulates an ordering system for a café named Java Journeys.
# It allows users to select from a variety of coffee, tea, and sweet treats,
# customize their choices (size, milk type, sugar level, etc.), and view their order total.
# The program supports command line arguments to initiate specific actions like 'order' or 'view'.
# It also features dynamic input validation, API calls for daily jokes, and JSON file handling for order saving.
    

def main():
    print()
    print()
    print()
    print("Welcome to Java Journeys Café!\n")
    # Checks to see if the user indicates Java Journeys is out of food items
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        if(first_arg == 'nf'):
            print("Please note we are not serving food items today/n")
    
    print("Joke of the day: ", get_random_joke())
    
    file_name = input("Please enter the name of the file containing your name: ")
    
    try:
        with open(file_name, 'r') as file:
            names = file.readlines()
        names = [name.strip() for name in names]  
        print(f"Welcome {names[1]}")
    except FileNotFoundError:
        print("Names file not found. Proceeding without name.")
        names = []


    order = []
    menuSelection(order)


def menuSelection(order):
    print()
    printMainMenu()
    menu_selection = inputValidation(3, printMainMenu)

    # Coffee & Espresso Drinks
    if menu_selection == 1:
        print("Coffee & Espresso Drinks:")
        printCoffeeMenu()
        menu_selection = inputValidation(10, printCoffeeMenu)

        #Return to main
        if menu_selection == 0:
            menuSelection(order)
            return
        
        #Espresso input
        elif menu_selection == 2:
            size, price = sizeInput()
            item = orders.Espresso(size)
            item.price += price

            order.append(item)
            print(f"Added a {item.describe()} to your order!")

        #All other options
        else:
            coffee_types = {
                1: "Brewed Coffee",
                2: "Espresso",
                3: "Americano",
                4: "Cappuccino",
                5: "Latte",
                6: "Mocha",
                7: "Iced Coffee",
                8: "Iced Latte",
                9: "Cold Brew",
                10: "Seasonal Special: Pumpkin Spice Latte"
            }

            # Takes user inputs
            type = coffee_types[menu_selection]
            size, price = sizeInput()
            milk = milkInput()
            sugar = sugarInput()

            item = orders.Coffee(size, milk, sugar, type)
            item.price += price

            # Adds item to order
            order.append(item)
            print(f"Added a {item.describe()} to your order!")

    # Tea & Other Beverages:
    elif menu_selection == 2:
        print("Tea & Other Beverages:")
        printTeaMenu()
        menu_selection = inputValidation(5, printTeaMenu)
        
        item = ""

        #Return to main
        if menu_selection == 0:
            menuSelection(order)
            return
        # Tea input
        elif menu_selection == 1:
            size, price = sizeInput()
            sugar = sugarInput()
            type = teaInput()
            item = orders.Tea(size, sugar, type)
            item.price += price
        # Chai input
        elif menu_selection == 2:
            size, price = sizeInput()
            sugar = sugarInput()
            milk = milkInput()
            item = orders.Chai(size, sugar, milk)
            item.price += price
        # Hot Chocolate input
        elif menu_selection == 3:
            size, price = sizeInput()
            milk = milkInput()
            item = orders.HotChocolate(size, milk)
            item.price += price
        # Lemonade
        elif menu_selection == 4:
            size, price = sizeInput()
            item = orders.Lemonade(size)
            item.price += price
        # Iced Tea
        elif menu_selection == 5:
            size, price = sizeInput()
            sweet = sweetInput()
            item = orders.IcedTea(size, sweet)
            item.price += price

        # Add to order
        order.append(item)
        print(f"Added a {item.describe()} to your order!")
        
    # Sweet Treats
    elif menu_selection == 3:
        print("Sweet Treats:")
        printSweetMenu()
        menu_selection = inputValidation(4, printSweetMenu)
        
        #Return to main
        if menu_selection == 0:
            menuSelection(order)
            return
        # Cookie input
        elif menu_selection == 1:
            type = cookieInput()
            warmed = warmedInput()
            item = orders.Cookie(type, warmed)
        # Brownie input
        elif menu_selection == 2:
            warmed = warmedInput()
            item = orders.Brownie(warmed)
        # Scone input
        elif menu_selection == 3:
            type = sconeInput()
            warmed = warmedInput()
            item = orders.Scone(type, warmed)
        # Cheesecake input
        elif menu_selection == 4:
            type = cheesecakeInput()
            item = orders.Cheesecake(type)

        # Add to order
        order.append(item)
        print(f"Added a {item.describe()} to your order!")
    
    #Prints entire order after adding
    printOrder(order)
    total = 0
    for item in order:
        total += item.price
            
    formatted_total = "{:.2f}".format(total)

    print(f"Your order total is ${formatted_total}")

    # Determines if user wants to check out
    menu_selection = "Y"
    menu_options = ["y", "n"]
    while True:
        print()
        menu_selection = input("Proceed to Checkout(Y or N)?")
        print()

        if menu_selection in menu_options:
            break
        else:
            print(f"{menu_selection} is not a valid selection")
            print("Please select yes(y) or (n)")
            print()

    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
    if first_arg == 'nf':
        print("Oops! The cafe is out of food items today. We've had to remove all food items from your order")
        print()

        for item in order:
            if item.isFood() == True:
                print(f"We've removed {item.describe()} from your order")
                order.remove(item)

    # Prints total or restarts depending on input
    if menu_selection == "y":
        printOrder(order)
        total = 0
        for item in order:
            total += item.price
            
        formatted_total = "{:.2f}".format(total)

        print(f"Your order total is ${formatted_total}")
        
        # saves order to order.json
        order_dicts = [item.to_dict() for item in order]
        with open("order.json", "w") as file:
            json.dump(order_dicts, file, indent=4)
            
    elif menu_selection == "n":
        menuSelection(order)

# validates input based on specified range
def inputValidation(size, print_function):
    """
    Validates user input ensuring it's within a specified range.

    This function prompts the user to make a selection from a range of menu options. 
    It validates the input to ensure it is within the given range (1 to 'size'). 
    If the input is not valid, it displays an error message and prompts the user again, 
    using the 'print_function' to display the menu options.

    Parameters:
    size (int): The upper limit of the range for valid input.
    print_function (function): A function with no parameters that prints the menu options.

    Returns:
    int: The validated menu selection made by the user, as an integer.
    """
    menu_options =[]
    for i in range(size + 1):
        menu_options.append(str(i))

    while True:
        print()
        menu_selection = input(f"Enter a selection from (1-{size}): ")
        print()

        if menu_selection in menu_options:
            menu_selection = int(menu_selection)
            break
        else:
            print()
            print(fr"{menu_selection} is not a valid selection ¯\_(ツ)_/¯")
            print("Please select from one of the following options...")
            print_function()
            print()
    
    return menu_selection


# API call to make random joke
def get_random_joke():
    try:
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url)
        response.raise_for_status()  
        
        joke_data = response.json()
        if joke_data["type"] == "single": 
            return joke_data["joke"]
        else:  
            return joke_data["setup"] + " - " + joke_data["delivery"]
    except requests.RequestException as e:
        return f"Error: {e}"

# Print customer order
def printOrder(order):
    print("Your Order: ")
    for item in order:
        print(indent(item.describe(), item.price))

# Handle formatting for  input
def indent(input, price):
    while(len(input) < 70):
        input += "."

    formatted_price = "{:.2f}".format(price)
    input += f"${formatted_price}"

    return input

# Handle size input
def sizeInput():
    print()
    print("Size: ")
    printSize()
    size_choice = inputValidation(3, printSize)
    size_types = {
        1: ("Small", 0.00), 
        2: ("Medium", 1.00),
        3: ("Large", 2.00)
    }
    size = size_types.get(size_choice, "Small") 
    
    size, price = size_types.get(size_choice, ("Small", 1.00))
    return size, price
    
# Handle milk input
def milkInput():
    print()
    print("Milk: ")
    printMilk()
    milk_choice = inputValidation(3, printMilk)
    milk_types = {1: "whole", 2: "oat", 3: "soy"}
    milk = milk_types.get(milk_choice, "whole") 
    return milk

# Handle sugar input
def sugarInput():
    print()
    print("Sugar: ")
    printSugar()
    sugar_choice = inputValidation(5, printSugar)
    sugar_types = {1: "0", 2: "25", 3: "50", 4: "75", 5: "100"}
    sugar = sugar_types.get(sugar_choice, "100") 
    return sugar

# Handle tea input
def teaInput():
    print()
    print("Type: ")
    printTea()
    tea_choice = inputValidation(3, printTea)
    tea_types = {1: "Black", 2: "Green", 3: "Herbal"}
    tea = tea_types.get(tea_choice, True) 
    return tea


# Handle sweet input
def sweetInput():
    print()
    print("Sweetness: ")
    printSweet()
    sweet_choice = inputValidation(2, printSweet)
    sweet_types = {1: True, 2: False}
    sweet = sweet_types.get(sweet_choice, True) 
    return sweet

# Handle warmed input
def warmedInput():
    print()
    print("Warmed:1 ")
    printWarmed()
    warmed_choice = inputValidation(2, printWarmed)
    warmed_types = {1: True, 2: False}
    warmed = warmed_types.get(warmed_choice, True) 
    return warmed

# Handle croissant input
def croissantInput():
    print()
    print("Type: ")
    printCroissant()
    croissant_choice = inputValidation(2, printCroissant)
    croissant_types = {1: "regular", 2: "chocoloate"}
    croissant = croissant_types.get(croissant_choice, "regular") 
    return croissant

# Handle muffin input
def muffinInput():
    print()
    print("Type: ")
    printMuffin()
    muffin_choice = inputValidation(4, printMuffin)
    muffin_types = {1: "Blueberry", 2: "Banana", 3: "Chocolate", 4: "Corn"}
    muffin = muffin_types.get(muffin_choice, "Blueberry") 
    return muffin

# Handle cream cheese input
def creamCheeseInput():
    print()
    print("Cream Cheese: ")
    printCreamcheese()
    creamCheese_choice = inputValidation(2, printCreamcheese)
    creamCheese_types = {1: True, 2: False}
    creamCheese = creamCheese_types.get(creamCheese_choice, True) 
    return creamCheese

# Handle cookie input
def cookieInput():
    print()
    print("Type: ")
    printCookie()
    cookie_choice = inputValidation(3, printCookie)
    cookie_types = {1: "Chocolate-chip", 2: "Oatmeal raisin", 3: "Sugar"}
    cookie = cookie_types.get(cookie_choice, "Chocolate-chip") 
    return cookie

# Handle scone input
def sconeInput():
    print()
    print("Type: ")
    printScone()
    scone_choice = inputValidation(3, printScone)
    scone_types = {1: "Blueberry", 2: "Lemon", 3: "Poppy Seed"}
    scone = scone_types.get(scone_choice, "Blueberry") 
    return scone

# Handle cheesecake input
def cheesecakeInput():
    print()
    print("Type: ")
    printCheesecake()
    cheesecake_choice = inputValidation(3, printCheesecake)
    cheesecake_types = {1: "Regular", 2: "Chocolate", 3: "Red Velvet"}
    cheesecake = cheesecake_types.get(cheesecake_choice, 1) 
    return cheesecake

# print size
def printSize():
    print("1) Small")
    print("2) Medium")
    print("3) Large")

# print milk
def printMilk():
    print("1) Whole")
    print("2) Oat")
    print("3) Soy")

# print sugar
def printSugar():
    print("1) 0%")
    print("2) 25%")
    print("3) 50")
    print("4) 75")
    print("5) 100")

# print tea
def printTea():
    print("1) Black")
    print("2) Green")
    print("3) Herbal")

# print sweet
def printSweet(): 
    print("1) Sweetened")
    print("2) Unsweetened")

# print warmed
def printWarmed(): 
    print("1) Yes")
    print("2) No")

# print croissant
def printCroissant(): 
    print("1) Regular")
    print("2) Chocolate")

# print muffin
def printMuffin():
    print("1) Blueberry")
    print("2) Banana")
    print("3) Chocolate")
    print("4) Corn")

# print creamcheese
def printCreamcheese():
    print("1) Yes")
    print("2) No")

# print cookie
def printCookie():
    print("1) Chocolate-chip")
    print("2) Oatmeal raisin")
    print("3) Sugar")

# print scone
def printScone():
    print("1) Blueberry")
    print("2) Lemon")
    print("3) Poppy Seed")

# print cheesecake
def printCheesecake():
    print("1) Regular")
    print("2) Chocolate")
    print("3) Red Velvet")


# PRINT MENU FUNCTIONS

## Main Menu
def printMainMenu():
    print(" 1) Coffee & Espresso Drinks")
    print(" 2) Tea & Other Beverages")
    print(" 3) Sweet Treats")
    print()

## Coffee & Espresso Drinks Menu
def printCoffeeMenu():
    menu_items = {
        1: ("Brewed Coffee", 2.50),
        2: ("Espresso", 2.00),
        3: ("Americano", 2.75),
        4: ("Cappuccino", 3.50),
        5: ("Latte", 4.00),
        6: ("Mocha", 4.50),
        7: ("Iced Coffee", 3.00),
        8: ("Iced Latte", 4.00),
        9: ("Cold Brew", 3.50),
        10: ("Seasonal Special: Pumpkin Spice Latte", 4.50)
    }

    for number, (name, price) in menu_items.items():
        print(f" {number}) {name.ljust(40, '.')} ${price:.2f}")
    print()


## Tea & Other Beverages Menu
def printTeaMenu():
    print(" 1) Assorted Teas..............................$2.00")
    print(" 2) Chai Latte.................................$3.50")
    print(" 3) Hot Chocolate..............................$3.00")
    print(" 4) Fresh Lemonade.............................$2.50")
    print(" 5) Iced Tea...................................$2.50")
    print()

## Sweet Treats Menu
def printSweetMenu():
    print(" 1) Cookies....................................$1.50")
    print(" 2) Brownies...................................$2.00")
    print(" 3) Scones.....................................$2.75")
    print(" 4) Cheesecake Slice...........................$4.00")
    print()

# Calls main
main()