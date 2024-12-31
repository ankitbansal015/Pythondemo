def names():
    import time
    names={"harry" , "ankit" , "yash" , "harshit", "tyagi","mannu","haris"}
    time.sleep(2)
    while True:
        text=(yield )
        if text in names:
            print("your name is in the list")
        else:
            print("your name is not in list")

name=names()
next(name)
name.send(input("type your name"))
name.close()