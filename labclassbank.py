class Bank:
    def openaccount(self,cname,acno,balance):
        self.acno=acno
        self.balance=balance
        self.cname=cname
        print("Hello ",cname,"Your account number",acno,"Is opened with",balance,"Rs.")
        
    def deposit(self,amount):
        self.amount=self.balance+amount
    def Withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("sorry u need another balance",balance)
    def checkbalance(self,balance):
        print("current balance : ",balance)


b1=Bank()
b1.openaccount("kajal",201,5000)

while True:
    print("1. deposit")
    print("2.withdraw")
    print("3.checkbalance")
    print("4.Exit")

    choice=int(input("Enter your choice : "))

    if choice ==1:
        amount=int(input("Enter deposit ammount : "))
        b1.deposit(amount)
        print("*"*60)
    elif choice ==2:
        amount=int(input("Enter withdraw ammount : "))
        b1.withdraw(amount)
        print("*"*60)
    elif choice ==3:
        b1.checkbalance(amount)
        print("*"*60)
    elif choice ==4:
        print("Thank you for using our services")
        print("*"*60)
        break
    else:
        print("Invalied choice.Plz try again")
        print("*"*60)


    
    
    
