import os
print(dir(os))
print(os.getcwd())
#for chnage the dirctory
# os.chdir("C//")
print(os.listdir())
# for list of any directory
# print(os.listdir("C://"))
# for making folder
# os.mkdir("this")
# for making directories
# os.makedirs("this/that")

#for renaming of file
# os.rename("ankit.txt","code of ankit.txt")

#for reading environment variables
# print(os.environ.get('path'))

# #for joinning path
# os.path.join("C://","ankit.txt")

#for cheking directory exists or not
print(os.path.exists("C://"))


print(os.path.isdir("C://"))