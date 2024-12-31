n= input("enter string")
# s=0
# w=
# for i in n:
#     s=s+1
#     if i =='char':
#         w=w+1
#
# print("char",w)
# print("total words",s+1)
char_count=0
word=1
for i in n:
    if(i.isalpha()):
        char_count=char_count+1
    elif(i.isspace()):
        word=word+1
print("total word",word)
print("total char",char_count)

