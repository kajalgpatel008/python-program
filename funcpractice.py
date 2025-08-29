class Bank:
    def account(self,acno,cname,balance):
        self.acno=acno
        self.balance=balance
        self.cname=cname
    def withdraw(self,amount):
        if amount>=self.balance:
            print("you need another balance",amount-self.balance)
        else:
            self.balance=self.balance-amount
    def deposit(self,amount):
        self.balance=self.balance+amount
    def checkbalance(self):
        print("current balance :",self.balance)
    

b=Bank()
b.account(101,"kajal",1000)

    
while True:
    print("1 : withdraw")
    print("2 : deposit")
    print("3 : balance")
    print("4 : exit")

    choice=int(input("Enter your choice :"))

    if choice==1:
        amount=int(input("Enter Withdraw amount : "))
        b.withdraw(amount)
    elif choice==2:
        amount=int(input("Enter Deposit amount : "))
        b.deposit(amount)
        
    elif choice==3:
        b.checkbalance()
    elif choice==4:
        print("Thank you for using our services")
        exit
    else:
        print("Invalied choice")
    
