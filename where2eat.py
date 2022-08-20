# Lists for storing data
    # This will eventually be moved to databases

eastside_restaurants = ['Chic-fil-a', 'Applebees', 'Japan House', 'Fuji', 'Panera Bread']
westside_restaurants = ['Chic-fil-a', 'Apollos', 'Fuji', 'Fuddruckers', 'Panera Bread']
downtown_restaurants = ['Sammich Shop', 'Monsoon', 'Nacho Taco', 'Sofias']
all_restaurants = ['Chic-fil-a', 'Applebees', 'Japan House', 'Fuji', 'Panera Bread', 'Apollos', 'Fuddruckers', 'Sammich Shop', 'Monsoon', 'Nacho Taco', 'Sofias']
favorite_restaurants = []

# Home Page Options:
# (1) Search for Restaurant
# (3) View Restaurants
# (3) Add Restaurant

def home_options():
    
    action = input("\nWhat do you want to do? \n(1) Search for Restaurant \n(2) View Restaurants \n(3) Add Restaurant \n\n>>>: ").lower().strip().title()

    if action == "1" or action == "Search" or action == "Search For" or action == "Search for Restaurant":
        search_options()

    elif action == "2" or action == "View" or action == "View Restaurant":
        view_options()

    elif action == "3" or action == "Add" or action == "Add Restaurant":
        add_options()

    else:
        print("\nSorry, that was an unrecognized command.")
        home_options()

# Search for Restaurant Options:

def search_options():

    from random import choice

    action = input("\nWhere are you / Where do you want to eat? \n(1) Eastside \n(2) Westside \n(3) Downtown \n(4) Anywhere! \n\n>>>: ").lower().strip().title()

    # Change the print text to display a message with the random resturant inside the string.

    if action == "1" or action == "East" or action == "Eastside":
        print("\n")
        print(choice(eastside_restaurants))
        print("\n")
        home_options()

    elif action == "2" or action == "West" or action == "Westside":
        print("\n")
        print(choice(westside_restaurants))
        print("\n")
        home_options()

    elif action == "3" or action == "Down" or action == "Downtown":
        print("\n")
        print(choice(downtown_restaurants))
        print("\n")
        home_options()

    elif action == "4" or action == "Any" or action == "Anywhere" or action == "Anywhere!":
        print("\n")
        print(choice(all_restaurants))
        print("\n")
        home_options()

    else:
        print("\n")
        print("Sorry, that was an unrecognized command.")
        search_options()

# View Restaurants Options:
# (1) Location
# (2) All
# (3) Favorites

def view_options():

    def locations():
        action = input("\nWhich Spartanburg location would you like to view? \n(1) Eastside \n(2) Westside \n(3) Downtown \n\n>>>: ").lower().strip().title()

        if action == "1" or action == "East" or action == "Eastside":
            print(eastside_restaurants)
            home_options()

        elif action == "2" or action == "West" or action == "Westside":
            print(westside_restaurants)
            home_options()

        elif action == "3" or action == "Down" or action == "Downtown":
            print(downtown_restaurants)
            home_options()

        else:
            print("\nSorry, that was an unrecognized command.")
            locations()
        
    action = input("\nWhat Restaurants would you like to view? \n(1) Location \n(2) All \n(3) Favorites \n\n>>>: ").lower().strip().title()

    if action == "1" or action == "Location":
        locations()

    elif action == "2" or action == "All":
        print(all_restaurants)
        home_options()

    elif action == "3" or action == "Favorites":
        print(favorite_restaurants)
        home_options()

    else:
        print("Sorry, that was an unrecognized command.")
        view_options()

# [Add Restaurant] Options asking where restaurant is located:
# (1) Eastside
# (2) Westside
# (3) Downtown

def add_options():

    def locations():

        action = input("\nWhere is the restaurant located? \n(1) Eastside \n(2) Westside \n(3) Downtown \n\n>>>: ").lower().strip().title()
    
        if action == "1" or action == "Eastside" or action == "East":
            restaurant = input("\nWhat's the Restaurant's name?: \n>>>: ").lower().strip().title()
            eastside_restaurants.append(restaurant)
            all_restaurants.append(restaurant)
            print(f"{restaurant} added to Eastside Restaurants!")
            home_options()

        elif action == "2" or action == "Westside" or action == "West":
            restaurant = input("\nWhat's the Restaurant's name?: \n>>>: ").lower().strip().title()
            westside_restaurants.append(restaurant)
            print(f"{restaurant} added to Westside Restaurants!")
            home_options()

        elif action == "3" or action == "Downtown" or action == "Down":
            restaurant = input("\nWhat's the Restaurant's name?: \n>>>: ").lower().strip().title()
            downtown_restaurants.append(restaurant)
            print(f"{restaurant} added to Downtown Restaurants!")
            home_options()

        else:
            print("\nSorry, that was an unrecognized command.")
            add_options()
    
    def favorites():

        print("\nWhich Restaurant did you want to add to Favorites?:") # Fix output for list formatting
        for restaurant in all_restaurants:
            print(restaurant)
        action = input("\n>>>: ").lower().strip().title()
        favorite_restaurants.append(action)
        print(f"{action} added to Favorites!")
        home_options()

    action = input("\nIs this a new add or are you adding a current restaurant to your favorites? \n(1) New Add \n(2) Favorites \n\n>>>: ").lower().strip().title()

    if action == "1" or action == "New" or action == "New Add" or action == "Add New":
        locations()
    
    elif action == "2" or action == "Favorites":
        favorites()
    
    else:
        print("\nSorry, that was an unrecognized command.")
        add_options()

home_options()