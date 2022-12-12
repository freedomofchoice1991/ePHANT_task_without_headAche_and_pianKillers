# !/usr/bin/env/python3
# Copyright ©rezaKarami

import random
import string

##-> this function chooses a random number between 6 to 13
##-> then save it in a temporary variable
def randName ():
    randomNameLength = (6,7,8,9,10,11,12,13)
    L = random.choice(randomNameLength)
    res = ''
    ##-> for the range of the temporary variable it adds a random ascii letter
    for i in range (1,L):
        res += random.choice(string.ascii_letters)
    ##-> the function return a random name     
    return(res)    

#######

##-> Using the randName() for 2 types of customers
def generateName ():  
    CustomerTypes = ('S','P')
    randomCustomerType = random.choice (CustomerTypes)
    ##-> use it to return only one random name if the customer is single
    if randomCustomerType == 'S':
        name = randName()
        return (name)
    ##-> use it to return 2 random names if the customer is pair    
    elif randomCustomerType == 'P':
        name1 = randName()
        name2 = randName()
        return (name1,name2)

