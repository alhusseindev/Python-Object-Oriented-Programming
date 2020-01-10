class Accounts:
    #Accounts class represents accounts in a banking system

    #Interest of 3%
    acc_intrst=1.03
    
    def __init__(self,fname, lname, intldeposit, balance=0):
        #create a member in the account
        self.fname= fname
        self.lname= lname
        self.intldeposit=intldeposit
        self.balance=balance+self.intldeposit
    def __str__(self):
        return "{}{}{}".format(self.fname,self.lname,self.balance)

    
    def deposit(self,damount):
        #make a deposit
        self.deposit=damount
        self.balance+=damount
        return self.balance
    
    def withdraw(self,wamount):
        #withdraw money
        if wamount>self.balance:
            raise RuntimeError("Invalid Transaction")
        self.balance-=wamount
        return self.balance

    
    def feecalculation(self):
        #fee calculation $10 if <1000 , $20 if >1000
        if self.balance<1000:
            self.balance=self.balance -10
        elif self.balance>=1000:
            self.balance=self.balance -20
        
    def interest(self):
        #calculate interest of 3%
        self.balance=float(self.balance*self.acc_intrst)

acc1=Accounts('Alhussein ', 'Eweis ', 10000 )
print(acc1)
acc1.deposit(56)
print(acc1)
acc1.withdraw(20)
print(acc1)
acc1.feecalculation()
print(acc1)
acc1.interest()
print(acc1)

acc2=Accounts('Some ', 'One ', 899)
print(acc2)
acc2.deposit(43)
print(acc2)
acc2.withdraw(10)
print(acc2)
acc2.feecalculation()
print(acc2)
acc2.interest()
print(acc2)

