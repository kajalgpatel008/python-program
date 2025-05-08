def test(a,b,c,d):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(1,2,3,4)

def test(a,b,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(1,2)

def test(a,b=30,c=30,d=40):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(1)



def test(a=40,b=30,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(b=100,d=200)
