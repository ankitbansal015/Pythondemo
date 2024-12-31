v=int(input())
w=int(input())
if (w&1)==1 or w<2 or w<=v:
    print("invalid")
else:
    x=((4*v)-w)//2
    print("TW={0} FW={1}".format(x,v-x))