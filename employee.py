"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from enum import Enum


class ContractType(Enum):
    Monthly = 0 
    Hourly = 1

class CommissionType(Enum):
    NoCommission = 0
    Contract = 1
    Bonus = 2

class Commission:
    def __init__(self, commissionType, amount):
        self.commissionType = commissionType
        self.amount = amount
        self.contracts = 1

    def set_contracts(self, contracts):
        self.contracts = contracts

    def get_contracts(self):
        return self.contracts

    def get_commissionType(self):
        return self.commissionType

    def get_amount(self):
        return self.amount


class Employee:
    def __init__(self, name, contractType, wage, commission):
        self.name = name
        self.contractType = contractType
        self.wage = wage
        self.commission = commission
        self.hoursWorked = 1

    def get_pay(self):
        pay = 0

        if (self.contractType == ContractType.Monthly):
            pay = self.wage
        else:
            pay = self.wage * self.hoursWorked

        commission = 0

        if (self.commission != None):
            commission = self.commission.get_amount() * self.commission.get_contracts()
        
        return pay + commission

    def set_hoursWorked(self, hoursWorked):
        self.hoursWorked = hoursWorked


    def __str__(self):

        commissionStr = ""
        
        if (self.commission != None):
            if (self.commission.get_commissionType() == CommissionType.Contract):
                commissionStr = f" and receives a commission for {self.commission.get_contracts()} contracts at {self.commission.get_amount()}/contract"
            else:
                commissionStr = f" and receives a bonus commission of {self.commission.get_amount()}"

        if (self.contractType == ContractType.Monthly):
            return f"{self.name} works on a monthly salary of {self.wage}{commissionStr}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.wage}/hour{commissionStr}. Their total pay is {self.get_pay()}."

      

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ContractType.Monthly, 4000, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ContractType.Hourly, 25, None)
charlie.set_hoursWorked(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
reneeCommission = Commission(CommissionType.Contract, 200)
reneeCommission.set_contracts(4)
renee = Employee('Renee', ContractType.Monthly, 3000, reneeCommission)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
janCommission = Commission(CommissionType.Contract, 220)
janCommission.set_contracts(3)
jan = Employee('Jan', ContractType.Hourly, 25, janCommission)
jan.set_hoursWorked(150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbieCommission = Commission(CommissionType.Bonus, 1500)
robbie = Employee('Robbie', ContractType.Monthly, 2000, robbieCommission)
print("Robbie: " + str(robbie.get_pay()))
print("Robbie: " + robbie.__str__())
print()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
arielCommission = Commission(CommissionType.Bonus, 600)
ariel = Employee('Ariel', ContractType.Hourly, 30, arielCommission)
ariel.set_hoursWorked(120)
