class A:
    classvar1="i am class variable of a class a"
    def __init__(self):
        self.var1="i am inside class a constructor"
        self.classvar1="ins var in class a"
        self.special="special"
class B(A):
    classvar2 ="i am in class b"
    def __init__(self):
        super().__init__()
        print(super().classvar1)
        self.var1="i am inside class b constructor"
        self.classvar1="ins var in class b"

a=A()
b=B()
print(b.classvar1)
print(b.special,b.var1,b.classvar1)
