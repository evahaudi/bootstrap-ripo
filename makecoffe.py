# Step 1: Inputs needed
# - Boiling water
# - Instant coffee powder
# - Optional: Sugar
# - Optional: Milk

# Step 2: Steps to make a cup of instant coffee
def make_coffee():
    # Step 2.1: Boil water
    boil_water()

    # Step 2.2: Prepare coffee
    prepare_coffee()

    # Step 2.3: Optional - Add sugar
    add_sugar()

    # Step 2.4: Optional - Add milk
    add_milk()

    # Step 2.5: Serve coffee
    serve_coffee()

# Step 3: Functions for individual steps
def boil_water():
    print("1. Boil water in a kettle or pot.")

def prepare_coffee():
    print("2. Take a cup and add a teaspoon of instant coffee powder.")

def add_sugar():
    choice = input("3. Would you like to add sugar? (yes/no): ")
    if choice.lower() == 'yes':
        print("   - Add desired amount of sugar to the coffee.")

def add_milk():
    choice = input("4. Would you like to add milk? (yes/no): ")
    if choice.lower() == 'yes':
        print("   - Pour desired amount of milk into the coffee.")

def serve_coffee():
    print("5. Stir the coffee well and it is ready to be served.")

# Step 4: Make a cup of coffee
make_coffee()
