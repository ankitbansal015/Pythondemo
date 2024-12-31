class elecdevice():
    comp="is used to perform operations"
    camera="is used to capture moments"

class pocketdevice(elecdevice):
    calculator="is used for calculations"
    earpods="is used for listen songs"

class mobile(pocketdevice):
    nokia="unbreakable"

asus_1=elecdevice
ear_pods=pocketdevice
nokia_2=mobile

print(nokia_2.camera)
