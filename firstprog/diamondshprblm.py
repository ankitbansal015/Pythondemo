class A:
    def met(self):
        print("this is a method from clss A")

class B(A):
    def met(self):
        print("this is a method from clss B")
class C(A):
    def met(self):
        print("this is a method from clss C")
class D(C,B):
    def met(self):
        print("this is a method from clss D")


a=A()
b=B()
c=C()
d=D()

d.met()