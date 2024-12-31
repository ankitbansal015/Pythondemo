# i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print((i+1), end=" ")
#     i = i + 1;
#     if(i==44):
#         break
#
while(True):
    inp = int(input("enter a num\n"))
    if inp>100:
        print("cong u have entered a number greter then 100\n")
        break
    else:
        print("try again")
        continue
