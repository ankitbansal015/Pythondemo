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

harry = employee("harry",121,"instructor")
rohan = employee("rohan",333,"student")
karan=employee.from_dash("karan-555-student")
employee.printgood("karan"
                   )
print(karan.printdetails())
# harry.name="harry"
# harry.salary=5566
#
# rohan.name="rohan"
# rohan.salary=541521
# print(harry.salary)
# print(harry.no_of_leaves)
# print(harry.__dict__)
# harry.no_of_leaves=2213
# print(harry.__dict__)
# employee.no_of_leaves=15
#print(harry.no_of_leaves)
