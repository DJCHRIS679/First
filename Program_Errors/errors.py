def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("Dividing by zero")

print(divide(1,0))
