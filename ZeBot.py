print("=" * 32)
print("      Welcome to ZeBot")
print("=" * 32)

name = input("Enter your name: ")

print("Hello,", name + "!")
print("I am ZeBot.")
print("Type 'help' to see available commands.")

while True:

    command = input("\nYou: ").lower()

    if command == "hello":
        print("ZeBot: Hello", name + "!")

    elif command == "how are you":
        print("ZeBot: I am doing great. Thanks for asking!")

    elif command == "your name":
        print("ZeBot: My name is ZeBot.")

    elif command == "creator":
        print("ZeBot: I was created by Zeyan.")
        
    elif command == "good morning":
         print("ZeBot: Good morning", name + "! Have a great day.")

    elif command == "thank you":
         print("ZeBot: You're welcome!")

    elif command == "calculator":

        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result =", num1 +num2)

        elif operator == "-":
            print("Result =", num1- num2)

        elif operator == "*":
            print("Result =", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("ZeBot: Cannot divide by zero.")

        else:
            print("ZeBot: Invalid operator.")

    elif command == "help":
        print("\nAvailable Commands:")
        print("hello")
        print("how are you")
        print("your name")
        print("creator")
        print("good morning")
        print("thank you")
        print("calculator")
        print("help")
        print("bye")

    elif command == "bye":
        print("ZeBot: Goodbye", name + "!")
        break

    else:
        print("ZeBot: Sorry, I don't understand that command.")