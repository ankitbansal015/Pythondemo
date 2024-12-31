# a=input("what your name")
# b= input("how much u earn")
# if int(b)==0:
#     raise  ZeroDivisionError("b is zero stoping program")
# if a.isnumeric():
#     raise  Exception("num are not allow")
#
# print(f"hello{a}")
c= input("enter your name")
try:
    print(a)

except Exception as e:
   if c=="harry":
       raise ValueError("harry is blocked ")
   print("exception handled")