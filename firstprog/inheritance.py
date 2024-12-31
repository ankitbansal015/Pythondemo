class employee:
    no_of_leaves=12
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
class programmer(employee):
    #overriding no of leaves
    no_of_leaves = 56
    def __init__(self,name,salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"the name is {self.name}.salary is {self.salary}. and role is {self.role}.the languages are {self.languages}"

harry =programmer("harry",121,"instructor",["c"])
rohan =programmer("rohan",333,"student",["cpp"])

shubh=programmer("shubh",656,"programmer",["python"])
karan=programmer("karan",689,"programmer",["python"])
print(karan.printprog())
print(harry.no_of_leaves)