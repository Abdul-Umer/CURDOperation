import mysql
class ATM:
    def __init__(self):
        self.name = "Umer"
        self._bank = "HDFC"
        self.__pin = 5861
        self.balance = 10000
        self.__address='Karnataka'
        
    def check_pin(self):
        return self.__pin
    def withdraw(self,amount,pin):
        if self.balance>0 and self.balance>=amount:
            if self.__pin==pin:
                self.balance-=amount
            else:
                print('Incorrect Pin')
                self.balance=self.balance
        else:
            print('Insufficient Funds')
            
        return self.balance
    def deposite(self,amount,pin):
        if self.__pin==pin:
            self.balance+=amount
            print('Deposited Successfully!')
        else:
            print('Incorrect Pin')
        return self.balance
    
    def change_pin(self,newpin):
        self.__pin=newpin
        return(f'Pin Change Successfull {self.__pin}')

    def miniStatement(self):
        return f'Name is: {self.name},Bank is: {self._bank},Balance is: {self.balance}'



obj = ATM()

print(obj._ATM__pin) 
print(obj.withdraw(1000,5861))
print(obj.change_pin(1234))
print(obj.deposite(4500,1234))
print(obj.miniStatement())


