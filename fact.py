def factorial():
    number = int(input("Enter Number"))
    counter = number-1
    while counter > 1:
        number = number * counter
        counter = counter-1

    print("Factorial is : ",number)
    cal_again()

def welcome():
    print("Welcome! You are using Factorial Function with Python")

def cal_again():
    chose = input("Use Calculator Again \n Y for Yes \n N for no")
    if chose.upper()=="Y":
        factorial()

    elif chose.upper()=="N":
        print("See you later\n")
    else:
        print("Invalid Input!!!")
        cal_again()

welcome()
factorial()
print("Thanks for using me!!")