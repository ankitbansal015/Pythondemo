d1={"ankit":"burger","yash":"chole","tyagi":"cream",
    "lala":{"bussiness":"farzi",}}
#d1[120]="teacher"
#del d1[120]
#print(d1["lala"])
print(d1)
#d2=d1
d2=d1.copy()
del d2["lala"]
#print(d1.copy())
print(d1)
print(d2)
d1.update({"gupta":"toffee"})
print(d1)
print(d1.keys())
print(d1.items())