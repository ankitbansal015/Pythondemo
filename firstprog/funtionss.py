a=5
b=6
c=sum((a,b)) #built in function
print(c)
# for user def fumction we have to use def keyword
def function1(a,b):
    print("hello you r in function1\n",a-b)10
function1(6,7)
def function2(a,b):
    """This is a function which will calculate average of two numbers"""  # docstring
    average = (a+b)/2
   # print(average)
    return average

# v=function2(5,7)
# print(v)
print(function2.__doc__)