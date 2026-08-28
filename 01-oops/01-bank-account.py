class BankAccount:
    def __init__(self, accountNumber:str, balance:int , roi:int):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi
    def getSimpleInterest(self, time:int):
        si = (self.balance * time * self.roi)/ 100
        return si
    def getBalanceWithInterest(self, time:int):
        return self.balance + self.getSimpleInterest(time)

