# Starter code
items = [1, 2, 3, 4, 5]

try:
    item = items[6]
    print(item)
except IndexError:
    print("Index out of range. Please access a valid index within the list.")
