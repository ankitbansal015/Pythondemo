import random

lst = []
sum = 0
even=0
for i in range(0, 20):
    n = random.randint(0, 100)
    lst.append(n)
leng=len(lst)
print(f"list of {leng} random no is={lst}".format(leng,lst))

for index in lst:
    sum=sum+index

avg=sum/len(lst)
print(f"average of elememt in list= {avg}".format(avg))

import random

lst = []
sum = 0
even=0
for i in range(0, 20):
    n = random.randint(0, 100)
    lst.append(n)
leng=len(lst)
print(f"list of {leng} random no is={lst}".format(leng,lst))

for index in lst:
    sum=sum+index


avg=sum/len(lst)
print(f"average of elememt in list= {avg}".format(avg))

for index in lst:
    if index%2==0:
        even+=1

print("largest no in list is= ",max(lst)," and smallest in list is =",min(lst))
lst.sort()
print("2nd largest no in list is= ",lst[-2]," and 2nd smallest in list is =",lst[1])
print("even no in list=",even)
#
print("largest no in list is= ",max(lst)," and smallest in list is =",min(lst))
lst.sort()
print("2nd largest no in list is= ",lst[-2]," and 2nd smallest in list is =",lst[1])
print("even no in list=",even)