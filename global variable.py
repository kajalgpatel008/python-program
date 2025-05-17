global x
x=10
try:

   def test1():
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

except UnboundLocalError as e:
    print("Exception Caught :",e)
