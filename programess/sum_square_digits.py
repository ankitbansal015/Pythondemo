i=int(input("enter the digit:"))
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("sum of square of digits is ",sum)