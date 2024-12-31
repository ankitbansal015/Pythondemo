class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@ankitbansal015.com"

    def explain(self):
        return f"this employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set. please set it by using setter"
        return f"{self.fname}.{self.lname}@ankitbansal015.com"
    @email.setter
    def email(self,string):
        print("setting now....")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


hindustani_supporter=Employee("Hindustani","supporter")
ankit_bansal=Employee("Ankit","Bansal")
print(hindustani_supporter.email)


hindustani_supporter.fname="US"

print(hindustani_supporter.email)
hindustani_supporter.email="this.that@ankitbansal015.com"
print(hindustani_supporter.email)
del hindustani_supporter.email
print(hindustani_supporter.email)
skillf=Employee("skill","f")
o="this is string"
print(skillf.email)
# print(type("dds"))
# print(id("cxc,dx"))
# print(id("jbchjxbcjh"))
# print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))