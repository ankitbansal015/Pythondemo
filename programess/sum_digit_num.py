i=int(input("enter the number to find sum:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digits=",sum)