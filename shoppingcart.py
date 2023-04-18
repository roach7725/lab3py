# Creating an empty dictionary to store the products and their brands
shoppingCart = {}

# Priningt the welcome message
print("WELCOME TO THE AMANDO SHOPPING SITE")

# Creating a while loop to keep the program running until the user enters 4
while True:
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")

    # Asking the user to enter his choice
    choice = int(input("Enter your choice :"))

    # If the user enters 1, then add a new product to the cart
    if choice == 1:
        # Asking the user to enter the number of items to be added in the cart
        numItems = int(input("Enter the number of items to be added in the cart:"))

        # If the number of items is more than 5, then print a message saying that the cart is full
        if numItems > 5:
            print("Cart is full.")

        # If the number of items is less than 5, then add those items to the cart
        else:
            # Creating a for loop to add the items to the cart
            for i in range(numItems):
                # Asking the user to enter an item
                item = input("Enter an item:")

                # Asking the user to enter the brand name
                brand = input("Enter the brand Name:")

                # Adding the item and brand to the dictionary
                shoppingCart[item] = brand

            # Printing the items in the cart
            print("You added following items to the cart:")
            for item, brand in shoppingCart.items():
                print(item + ": " + brand)

    # If the user enters 2, then search for a product in the cart
    elif choice == 2:
        # Ask the user to enter the item to be searched
        searchItem = input("Enter the item to be searched:")

        # Searching for the item in the dictionary
        if searchItem in shoppingCart:
            print(searchItem + ": " + shoppingCart[searchItem])

        # If the item is not found in the dictionary, then print a message saying that no product exists with that name
        else:
            print("No product exists with this name.")

    # If the user enters 3, then delete a product from the cart
    elif choice == 3:
        # Asking the user to enter the item to be deleted
        deleteItem = input("Enter the item to be deleted:")

        # Deleting the item from the dictionary
        del shoppingCart[deleteItem]

        # Printing the items in the cart
        print("You added following items to the cart:")
        for item, brand in shoppingCart.items():
            print(item + ": " + brand)

    # If the user enters 4, then quit the program
    elif choice == 4:
        ("Thank you for shopping")
        break

    # If the user enters any other number, then print a message saying that the wrong option is entered
    else:
        print("Wrong Option Entered.")