def divide_by_zero():
    try:
        result = 5 / 0
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"


result = divide_by_zero()
print(result)