print("welcome to calculator")
num1=int(input("enter the 1 num:"))
num2=int(input("enter the 2 num:"))
operator = input("which operator u want to use?:")
if operator == '+':
    add = int(num1) + int(num2)
    print(" the addition of the 2 num is:", )
elif operator == '*':
    multiply = int(num1) * int(num2)
    print("the multiplication of 2 num is :",multiply)
elif operator == '-':
    subt = int(num1) - int(num2)
    print("the subtraction of 2 num is :", subt)
elif operator == '/':
    div = int(num1) / int(num2)
    print("the division of 2 num is :", div)
elif operator =='**':
    power = int(num1) ** int(num2)
    print("the power of  num1 to the power num2 :", power)

else:
    print("invalid")
