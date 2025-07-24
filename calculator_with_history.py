HISTORY_FILE="history.txt"    #This line defines a global constant HISTORY_FILE, which stores the name of the file where all calculations will be saved.

def show_history():
    file = open(HISTORY_FILE, 'r')  # Open file in read mode
    lines = file.readlines()        # Read all lines into a list

    if len(lines) == 0:
        print("No history found!")  # If file is empty
    else: 
        for line in reversed(lines):   # Print lines from latest to oldest
            print(line.strip())        # Remove newline characters
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')  # Open in write mode (this clears the file)
    file.close()                    # Immediately close
    print("History cleared.")


def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')             # Open in append mode
    file.write(equation + "=" + str(result) + "\n")  # Save result
    file.close()


def calculate(user_input):
    parts = user_input.split()  # Split input into 3 parts: num1 operator num2

    if len(parts) != 3:
        print("invalid input")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    # Perform operation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("can't divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    # Convert result to int if no decimal part
    if int(result) == result:
        result = int(result)

    print("Result:", result)

    # Save to history file
    save_to_history(user_input, result)


def main():
    print("_ _ _ SIMPLE CALCULATOR (type history, clear or exit)")

    while True:
        user_input = input("Enter calculation ( + - * / ) or command (history, clear or exit): ")

        if user_input == 'exit':
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input.upper())

main()