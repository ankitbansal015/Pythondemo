import pickle
# list=["audi","bmw","swift","kia"]
# file="mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(list,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))