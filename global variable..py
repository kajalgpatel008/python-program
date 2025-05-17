def test1():
    global x
    x=10
    global y
    y=20
    print("X : ",x)
    print("Y : ",y)
    x=x+100
def test2():
    print("X : ",x)
    print("Y : ",y)
test1()
test2()

