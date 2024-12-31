readdatafile=open("srudent3.txt",'r')

read=readdatafile.read()
li=read.split()
print(li)
new_format=li[2]+" "+li[1]+" "+" "+li[1][0:6:4]+"."
print(new_format)
new_format=li[5]+" "+li[4]+" "+" "+li[3][0:6:3]+"."
print(new_format)