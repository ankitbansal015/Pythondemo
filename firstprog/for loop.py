# list1 = [["ankit",1] , [ "pankit",5] , ["tankit",6] , ["hankit",9]]
# #print(list1) for printing list
# for item , pop  in list1:
#     print(item, "and pop is ",pop)
# dict1 =dict(list1)
# print(dict1)
# for item in dict1:
#     print(item)
list1=[1,2,5,8,7,9,6,3,66,8,8,7,9,9,6666,5,54,4444,454]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)