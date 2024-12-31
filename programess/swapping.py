# a = float(input(" Please Enter the First Value a: "))
# b = float(input(" Please Enter the Second Value b: "))
#
# print("Before Swapping two Number: a = {} and b = {}".format(a, b))
#
# temp = a
# a = b
# b = temp
#
# print("After Swapping two Number: a = {} and b = {}".format(a, b))

# def reverse(str):
#     str = input('enter your name: ')
#     for i in str:
#         str = i + str
#     return str
#
# print("\nThe original string is:",str)
# print("The reverse string is:", reverse(str))
# my_str = input("Please enter your own String : ")
# str = ''
# for i in my_str:
#     str = i + str
# print("\nThe Original String is: ", my_str)
# # print("The Reversed String is: ", str)
# n = int(input("Enter number of rows: "))

# for i in range(1,n+1):
#     A = 65
#     for j in range(1, i+1):
#         print("%c" %(A), end="")
#         A += 1
#     print()
n=int(input("enter a num: "))
i=1
while i<=n:
    d=i*i*i+1
    i+=1
    print(d,end=",")
