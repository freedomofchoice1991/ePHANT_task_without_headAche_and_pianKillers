# !/usr/bin/env/python3
# Copyright ©rezaKarami

from cmath import sin
import random
from genRandCusName_newTry import generateName 
from genRandCusName_newTry import genRandNameForFamily


class Customer:
    ##-> __init__ function is called automatically every time the calss is being used to create a new instance
    def __init__(self, name, money, type):
        self.name = name
        self.money = money
        self.type = type

    ##-> A function that gets an argument and decrease one from it
    def singleComeToRestaurant(y):
        return y - 1

    ##-> A function that gets an argument and decrease 2 from it
    def pairComeToRestaurant(y):
        return y -2
    
    ##-> A function that gets 2 arguments [restaurant seats and random number of family members] and decrease the second arg from the first one
    def familyComeToRestaurant(y,x):
        return y - x
    
    ##-> assuming each person pays 10 euro for food
    def singleCustomerPayForFood(x):
        return x + 10
    ##-> assuming each person pays 10 euro for food
    def pairCustomerPayForFood(x):
        return x + 20    
    
    ##-> assuming that family customer pay 100 euro each time comes to restaurant (for simplicity)
    def familyCustomerPayForFood(x):
        return x + 100

    ##-> A function that gets an argument and adds one to it
    def singleExitFromRestauant(y):
        return y + 1
    
    ##-> A function that gets an argument and adds 2 to it
    def pairExitFromRestaurant(y):
        return y + 2   
        


##----Generate 2k random customers----

##-> A list to keep the data for each pair customer
pairCustomerPool = []
##-> A list to keep the data for each single customer
singleCustomerPool = []

##-> A loop for 2000 times 
for customerInstance in range(1,2001):
    ##-> for each loop one instance gets created and whether it is single or pair gets random name
    customerInstance = generateName()
    ##-> after instance was created and recieved name its data gets saved into a temporary variable
    ##-> and gets a random amount of money between 50 to 100
    x = Customer(customerInstance,random.randint(50,100), type(customerInstance))
    ##-> Now based of the type of the instance we decide to keep it as single customer or pair customer
    if type(customerInstance) is tuple:
        pairCustomerPool.append(x)
    else:
        singleCustomerPool.append(x)   


##############STAGE 2#############
## Add one additional customer for Family. Family has 3-6 persons inside it.

##-> it was not defined so I allocated 500 euro for money
familyInstance = genRandNameForFamily()
fam = Customer(familyInstance, 500, list)

## 

