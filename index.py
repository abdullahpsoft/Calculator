def calculation():
    operator = input("ChoseOperation \n + For Addition \n - For Subtraction \n * For Multiplication \n / For Division")
    number_1 = int(input("Enter first number:"))
    number_2 = int(input("Enter second number:"))

    if operator == "+":
        print("Addition: ", number_1 + number_2)

    elif operator == "-":
        print("Subtraction: ", number_1 - number_2)

    elif operator == "*":
        print("Multiplication: ", number_2 * number_1)

    elif operator == "/":
        print("Division: ", number_1 / number_2)

    else:
        print("Invalid Operator!!!")

    cal_again()

def cal_again():
    chose = input("Use Calculator Again \n Y for Yes \n N for no")
    if chose.upper()=="Y":
        calculation()

    elif chose.upper()=="N":
        print("See you later\n")
    else:
        print("Invalid Input!!!")
        cal_again()

def welcome():
    print("Welcome! You are using Calculator with Python")

welcome()
calculation()
print("Thank you for using me!")