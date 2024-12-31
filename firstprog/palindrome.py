# str='ankit'
# strstr=str.casefold()
# rev=reversed(str)
# if list(str)==list(rev):
#     print("palindrome!")
# else:
#     print("not palindrome!")


num=int(input("enter a num:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("palindrome!")
else:
    print("not palindrome!")
print(rev)


