# !/usr/bin/env/python3
# Copyright ©rezaKarami
  
from customer_newTry import * 
from restaurant_newTry import *
from csv import writer


def main():

    ##-> Simulation of three months with While loop
    months = 1

    while months < 4:
        ##-> Print the beginning of each month as help to understand the code better
        print(f'\n\n\n******** month number {months} *********\n')
        ##-> pre-defined chances for each type of customer
        chanceSingleCustomer = 0.01
        chancePairCustomer = 0.02
        ##-> Counter for days of a month [30 day months are assumed]
        numberOfDays = 1
        ##-> saving the result of final busy seats for every day in one month
        listOfBusySeats = []
        ##-> saving the result of the amount of money restaurant gets from customers every day in one month [Assuming each person pays 10 euro for a meal]
        listOfRestaurantBalance = []
        
        ##-> using a While loop to get through 30 days in one month
        while (numberOfDays < 31):
            ##-> counter for each day busy seats
            today_busy_seats = 0
            ##-> counter for restaurant balance for each day of the month [after every loop it re-sets to 0 again]
            today_restaurant_balance = 0
            
            ##-> For loop for going through each hour which restaurant is open [6 hours every day]
            for hour in range(1,7):
                ##-> counter of how many single customer come to restaurant each hour
                singleCustomerCounter = 0
                ##-> counter of how many pair customers come to restaurant each hour
                pairCustomerCounter = 0
                
                ##-> random.random()  returns a random floating point number in the range [0.0, 1.0)
                ##-> This was used here to loop throuth every single-customer and if the floating random number
                ##-> was less than or equal pre-defined chance given by the challenge
                ##-> then we assume that single-customer came to the restaurant at that
                ##-> specific hour and plus 1 to the counter
                for s in singleCustomerPool:
                    if (random.random() <= chanceSingleCustomer):
                        singleCustomerCounter +=1
                        ##-> calling the function <singleComeToRestaurant> and giving the number of seats as argument
                        ##-> to it. It returns the number of seats minus 1
                        Restaurant.NumberOfSeats = Customer.singleComeToRestaurant(Restaurant.NumberOfSeats)
                        ##-> calling the funtion <singleCustomerPayForFood> and restaurant balance as argument to it 
                        ##-> assuming each person pays 10 euro, it returns the restaurant balance + 10
                        today_restaurant_balance += Customer.singleCustomerPayForFood(Restaurant.restaurantBalance)

                ##-> random.random()  returns a random floating point number in the range [0.0, 1.0)
                ##-> This was used here to loop throuth every pair-customers and if the floating random number
                ##-> was less than or equal pre-defined chance given by the challenge
                ##-> then we assume that pair-customer came to the restaurant at that
                ##-> specific hour and plus 1 to the counter
                for p in pairCustomerPool:
                    if (random.random() <= chancePairCustomer):
                        pairCustomerCounter +=1
                        ##-> calling the function <pairComeToRestaurant> and giving the number of seats as argument
                        ##-> to it. It returns the number of seats minus 2                        
                        Restaurant.NumberOfSeats = Customer.pairComeToRestaurant(Restaurant.NumberOfSeats)
                        ##-> calling the funtion <pairCustomerPayForFood> and restaurant balance as argument to it 
                        ##-> assuming each person pays 10 euro, it returns the restaurant balance + 20                        
                        today_restaurant_balance += Customer.pairCustomerPayForFood(Restaurant.restaurantBalance)

                ##-> calculating number of busy seats by adding the counter of single and pair customers
                ##-> needles to say that pair customers occupy 2 seats
                today_busy_seats += (singleCustomerCounter + (pairCustomerCounter * 2))
            
            ##-> Saving the number of busy seats for today before next loop begins [counter will be set to zero]
            listOfBusySeats.append(today_busy_seats)
            ##-> Saving the restaurant balance for today before next loop begins [counter will be set to zero]
            listOfRestaurantBalance.append(today_restaurant_balance)
            

            ##-> adds up counter of day in month to prevent infinite loop 
            numberOfDays += 1
        
        ##-> after each loop/month every single-customer gets randomly 50-100 euro
        for i in range(0, len(singleCustomerPool)):
            ##-> was not defined in the challenge whether if the customer keeps the money
            ##-> from the last month or not. So I reset it to zero and allocated a random amount to it
            singleCustomerPool[i].money = 0    
            singleCustomerPool[i].money += random.randint(50,100)
            
        ##-> at each loop/month every pair-customer gets randomly 50-100 euro
        for i in range(0, len(pairCustomerPool)):
            ##-> was not defined in the challenge whether if the customer keeps the money
            ##-> from the last month or not. So I reset it to zero and allocated a random amount to it
            pairCustomerPool[i].money = 0
            pairCustomerPool[i].money += random.randint(50,100)

        ##-> geting the minimum number from the list of busy seats in one month
        minBusySeats = min(listOfBusySeats)

       ##-> writing the data in to a CSV file (Append mode)
        with open("csv/dailyStatistics.csv", 'a') as file:   #creates a new file
            csv_writer = writer(file)
            ##-> writing the month number in a row
            csv_writer.writerow(["Month", "number", f"{months}"])
            ##-> writing the headers
            csv_writer.writerow(["day", "busy seats", "restaurant balance"])
            ##-> A loop for writing a row for every day of the month
            for i in range (1,31):
                ##-> Number of the day, Number of busy seats on that day, Balance of restaurant on that day
                csv_writer.writerow([i,listOfBusySeats[i-1],listOfRestaurantBalance[i-1]])
            ##-> At the end of every month
            ##-> writing a row for the total account balance of restaurant on that month    
            csv_writer.writerow(["Total", "balance",f"{sum(listOfRestaurantBalance)}"])
            ##-> writing a row for the minimum number of busy seats on that month 
            ##-> and defining on which day it was
            csv_writer.writerow(["Minimum number of busy seats", f"{minBusySeats}",f"on day {listOfBusySeats.index(minBusySeats) + 1}"])    
            ##-> seperator at the end of each month numbers
            csv_writer.writerow(["-----", "-----","-----"])    



        #################################################################################
        ####->     Creating a CSV file for each type of customers based on customer pools 
        #################################################################################
        ##-> Pair customers CSV list:
        with open("csv/pairCustomerPoolMembers.csv", 'a') as file:   #creates a new file
            csv_writer = writer(file)
            ##->  Writing the first row and defining the number of the month
            csv_writer.writerow(["Month","number",f"{months}","---"])
            ##-> writing the headers
            csv_writer.writerow(["number","Pair Customer Names","Customer Money", "CustomerType"])
            ##-> A loop for writing a row for every pair customer information
            for i in range(0,len(pairCustomerPool)):
                csv_writer.writerow([i+1,pairCustomerPool[i].name,pairCustomerPool[i].money, pairCustomerPool[i].type] )
            csv_writer.writerow(["---","---","---","---"])
            csv_writer.writerow(["---","---","---","---"])

        ##-> Single customers CSV list:
        with open("csv/singleCustomerPoolMembers.csv", 'a') as file:   #creates a new file
            csv_writer = writer(file)
            ##->  Writing the first row and defining the number of the month
            csv_writer.writerow(["Month","number",f"{months}","---"])
            ##-> Writing the headers
            csv_writer.writerow(["number","Single Customer Name","Customer Money", "CustomerType"])
            ##-> A loop for writing a row for every single customer information
            for i in range(0,len(singleCustomerPool)):
                csv_writer.writerow([i+1,singleCustomerPool[i].name,singleCustomerPool[i].money, singleCustomerPool[i].type] )
            csv_writer.writerow(["---","---","---","---"])
            csv_writer.writerow(["---","---","---","---"])    
        #################################################################################

        ##-> adds up counter of month to prevent infinite loop 
        months += 1 

    print('\n\n\n----- Success: please look into the csv folder in order to find results -------\n\n')

if __name__ == '__main__': main()     






######################################################################################
######### Stage 2 task
######################################################################################
### Restaurant pays costs randomly for three months

##-> calling the function 3 times for each month restaurant paid costs
for i in range (0,3):
    randomCostOfThisMonth = Restaurant.payCosts()
    print (f'The random costs restaurant paid in moth {i+1} is {randomCostOfThisMonth} euro')
    Restaurant.restaurantBalance += randomCostOfThisMonth

print(f'After 3 months of paying random costs between 100 to 500 by restaurant, the final amount is: {Restaurant.restaurantBalance} euro')
######################################################################################
######################################################################################







