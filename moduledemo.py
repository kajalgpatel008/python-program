import udf

while True:
    print("*"*50)
    print("1. Oddeven")
    print("2. Max of Two")
    print("3. Max of Three")
    print("4. fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*50)

    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        a=int(input("Enter value : "))
        udf.oddeven(a)
        print("*"*50)
    elif choice==2:
        a=int(input("Enter value : "))
        b=int(input("Enter value : "))
        udf.maxoftwo(a,b)
        print("*"*50)
    elif choice==3:
        a=int(input("Enter value : "))
        b=int(input("Enter value : "))
        c=int(input("Enter value : "))
        udf.maxofthree(a,b,c)
        print("*"*50)
    elif choice==4:
        a=int(input("Enter value : "))
        udf.fibonacci(a)
        print("*"*50)
    elif choice==5:
        a=int(input("Enter value : "))
        udf.prime(a)
        print("*"*50)
    elif choice==6:
       print("Thank you for using our service")
       print("*"*50)
       break
    else :
        print("Invalied choice. Please try again")
        print("*"*50)

  
              
              
