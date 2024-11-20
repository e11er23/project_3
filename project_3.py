#Project 3 python file

print("test")

#needs
#caregivers info
#schedules managment
# need to calculate payments
# need a calendar 

#cargiver class

#need name, number, email, pay rate, hours
#also need to handle availability 

import tkinter as tk
from tkinter import messagebox

class Cargiver:
    def __init__(self, name, number, email, pay_rate):
        """need to set up a cargivers details """
        self.name = name
        self.number = number
        self.email= email
        self.pay_rate = pay_rate
        self.availability = {} #empty cuz they will enter it

    def __str__(self):
        return f"({self.name}): {self.number}, {self.email}"
        # want it to show up like (Ryan): 443, x@terpmail

#class test
# ryan = Cargiver("Ryan", "443", "terpmail.umd.edu", 30)

# print(ryan)

# print(ryan.availability)