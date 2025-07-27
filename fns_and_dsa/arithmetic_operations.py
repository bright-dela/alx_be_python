def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return f"Oops! cannot divide by zero(0)."
        else:
            return num1 / num2


if __name__ == "__main__":
    print(perform_operation(1, 78, "Add"))
