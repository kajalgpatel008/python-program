class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C : ",self.c)
class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)
    
b1=B()
c1=C()
d1=D()

c1.getA(10)                ##any object in A,,b1.A,c1.A,d1.A
b1.getB(20)
c1.putA()
b1.putB()
c1.getC(30)
c1.putC()
d1.getD(40)
d1.putD()


