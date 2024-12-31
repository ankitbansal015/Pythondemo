# f= open("ankit2.txt","w")
# f.write("harry bhai bdiya h\n ")
# f.close()

#handle read and write both
f= open("ankit2.txt","r+")
print(f.read())
f.write("thnku\n")
f.write("harry bhai bdiya h\n ")
f.close()