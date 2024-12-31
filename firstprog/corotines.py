def searcher():
    import time

    book="this is the on ankit "
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("ypur text in book")
        else:
            print("your text not in book")

search=searcher()
print("search started")
next(search)
print("next method run")
search.send("ankit")
#for close coroutines
#search.close()
input("press any key")
search.send("on hh ankit")