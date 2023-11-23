def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"


ans = divide_by(40, 0)
print(ans)
