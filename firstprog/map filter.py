# numbers =["3","5","7"]
# numbers =list(map( int,numbers))

# for i in range (len(numbers)):
#     numbers[i]= int (numbers[i])

# numbers[2] = numbers[2] +1
# print(numbers[2])
# def sq(a):
#     return a*a
#
# num = [3,6,8,4,67]
# square = list(map(sq,num))
# print(square)

# num= [3,6,8,4,67]
# square=list(map(lambda x: x*x , num))
# print(square)
# def square (a):
#     return a*a
#
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for i in range (6):
#     val = list(map(lambda x:x(i),func))
#     print(val)

# list_1=[2,55,5,26,6,9]
# def is_gret_5(num):
#     return num>5
# gr_than_5 = list(filter(is_gret_5, list_1))
# print(gr_than_5)


from functools import reduce
list1 =[2,3,2,2,325,5,6]
num=reduce(lambda x,y:x+y,list1)
print(num)
# num=0
# for i in list1:
#     num= num + i
# print(num)