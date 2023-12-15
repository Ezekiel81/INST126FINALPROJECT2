## Readme for Java Journeys Café Ordering System
# Overview
Java Journeys Café Ordering System is a Python-based interactive command-line application that allows customers to order coffee, tea, other beverages, and sweet treats from a fictional café. The application includes a variety of functionalities, such as displaying menus, handling user inputs, adding items to the order, and calculating the total price.

# Features
Menu Selection: Users can select from a range of coffee, tea, and sweet treats.
Customizable Orders: Options for customizing beverages with different sizes, milk types, and sugar levels.
Order Review and Checkout: Users can review their order and proceed to checkout or modify the order.
Joke of the Day: The application displays a random joke each time it is run.
Saving Orders: Orders can be saved to a JSON file for record-keeping. 

# How to Run
Ensure you have Python installed on your system. No external libraries are required for the basic functionality of the system.
Run the following command:
python cafe_ordering_system.py

# Components
main(): The entry point of the application. It welcomes the user and initiates the menu selection process.
menuSelection(order): Handles the main menu and redirects to specific menus based on user choice.
inputValidation(size, print_function): Validates user inputs based on the provided options.
get_random_joke(): Fetches a random joke from an online API.
printOrder(order): Prints the current order along with prices.
sizeInput(), milkInput(), sugarInput(), teaInput(), sweetInput(), warmedInput(), cookieInput(), sconeInput(), cheesecakeInput(): Functions for handling various user inputs for customizing the order.
printSize(), printMilk(), printSugar(), printTea(), printSweet(), printWarmed(), printCookie(), printScone(), printCheesecake(): Functions to print options for each input type.
printMainMenu(), printCoffeeMenu(), printTeaMenu(), printSweetMenu(): Functions to display different menus.

# Advanced Topics
Advanced Strings: Advanced string methods are used throughout the program in the cafe_ordering_system.py and orders.py
JSON: Saves the file as a json
API: Random joke genarator
GIT: Check version control