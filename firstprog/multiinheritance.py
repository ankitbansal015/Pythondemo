class employee:
    no_of_leaves=12
    var=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"the name is {self.name}.salary is {self.salary}. and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good " +string)



class player:
    no_of_games=6
    var=6
    def __init__(self,name,game):
        self.name=name
        self.games=game
    def printdetails(self):
        return f"the name is {self.name}. game is {self.game}"
    #multilevel inheritance
class coolprogrammer(employee,player):
    language="C++"

    def printlanguage(self):
        print(self.language)
harry = employee("harry", 121, "instructor", )
rohan = employee("rohan", 333, "student", )

shubh=player("shubham",["cricket"],)
karan=coolprogrammer("karan",2565,"coolprogrammer")
det = karan.printdetails()
print(det)
karan.printlanguage()
print(karan.var)