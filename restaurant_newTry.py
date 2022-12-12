# !/usr/bin/env/python3
# Copyright ©rezaKarami

import random

class Restaurant:
    restaurantBalance = 0  ##-> was not defined so I allocated 0 to it
    NumberOfSeats = 500  ##-> was not defined so I persumed a number

    ##-> A function which returns a random number between 100 to 500 for costs of restaurant.
    def payCosts():
        randomCostForMonth = random.randint(100,500)
        return randomCostForMonth
