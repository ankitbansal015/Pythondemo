r=open("student.txt","rt")
w=open("student3.txt","w")
r.write("kamal kumar sharma\n")

data=r.readlines()

for i in data:
    name=i.split()
    s=(name[2]+" "+name[0][0]+name[0][1]+"."+name[1][0]+name[1][1]+"."+"\n")
    w.write(s)

r.close()
w.close()