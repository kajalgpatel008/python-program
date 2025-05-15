class A:
    def show(self):
        print("Show From class A")
class B(A):
    def show(self):
        super().show()
        print("Show From class B")
        
class C(B):
    def show(self):
        super().show()
        print("Show From class C")

c1=C()
c1.show()

        
