class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",cname,"your Account number ",acno,"Is opened With ",balance,"Rs.")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry you Need Another ",amount-self.balance,"Rs.")
    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()
print("*"*70)
b1.openAccount(101,"Maulik",1000)
print("*"*70)

while True:
    print("*"*70)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. checkBalance")
    print("4. Exit")
    print("*"*70)

    choice=int(input("Enter your Choice : "))

    if choice==1:
         amount=int(input("Enter Deposit Ammount : "))
         b1.deposit(amount)
         print("*"*70)
    elif choice==2:
        amount=int(input("Enter Withdrawal Ammount : "))
        b1.withdraw(amount)
        print("*"*70)
    elif choice==3:
        b1.checkBalance()
        print("*"*70)
    elif choice==4:
        print("Thank you for using Our Services")
        print("*"*70)
        break
    else:
        print("Invalied choice.Please Try Again")
        print("*"*70)
        
        
        















        
        
        

        
        




