menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float: The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    subtotal = 0.0  # Initialize subtotal
    for item in order:
        subtotal += item['price']  # Add the price of each item to the subtotal

        rounded_subtotal = float(f'{subtotal:.2f}')
    
    return rounded_subtotal


    raise NotImplementedError()

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tax_rate = 0.15  # 15% tax rate
    tax = subtotal * tax_rate  # Calculate the tax amount
    rounded_tax = round(tax, 2)  # Round the tax amount to two decimal places
    
    return float(rounded_tax)

    raise NotImplementedError()

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    print_order(order)
    ### WRITE SOLUTION HERE 
    # Calculate subtotal
    subtotal = sum(item['price'] for item in order)
    
    # Calculate tax
    tax_rate = 0.15  # 15% tax rate
    tax = subtotal * tax_rate
    
    # Calculate total (subtotal + tax)
    total = round(subtotal + tax, 2)
    
    # Store only the names of all items in the order in a list called names
    names = [item['name'] for item in order]
    
    return names, total

    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order



'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()

    # if order:
    #     print(f"You have ordered {len(order)} items")
    #     items_ordered = [item['name'] for item in order]
    #     print(items_ordered)
        
    #     subtotal = calculate_subtotal(items_ordered)
    #     print(f"Subtotal for the order is: ${subtotal:.2f}")
    # else:
    #     print("No items ordered.")

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    names, total = summarize_order(order)
    print("Summary of Order:")
    print("Items Ordered:", names)
    print("Total Cost:", total)

if __name__ == "__main__":
    main()
