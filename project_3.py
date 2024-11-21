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

# import tkinter as tk
# from tkinter import messagebox
#may not use anymore


# class Cargiver:
#     def __init__(self, name, number, email, pay_rate):
#         """need to set up a cargivers details """
#         self.name = name
#         self.number = number
#         self.email= email
#         self.pay_rate = pay_rate
#         self.availability = {} #empty cuz they will enter it

#     def __str__(self):
#         return f"({self.name}): {self.number}, {self.email}"
#         # want it to show up like (Ryan): 443, x@terpmail

#class test
# ryan = Cargiver("Ryan", "443", "terpmail.umd.edu", 30)

# print(ryan)

# print(ryan.availability)

#new logic for getting details

def input_caregiver_details():
    caregivers={} #empty for now
    num_caregivers= int(input("Enter the number of caregivers:\n")) 
    # I know the project says 8 but for the sake of testing it is easier to make it like 2 or 3

    for caregiver in range(num_caregivers):
        name= input("Enter caregiver's name:\n")
        phone = input(f"Enter {name}'s phone number:\n")
        email = input(f"Enter {name}'s email adress:\n")
        pay_rate = float(input(f"Enter {name}'s hourly pay rate (0 if unpaid)\n"))


        caregivers[name]= {
            "phone": phone,
            "email": email,
            "Pay_rate": pay_rate,
            "availability": {}, #empty at first but will store availability
            "assigned_hours": 0 #0 until they get assigned hours


        }

        print(f"\nSet availability for {name} (A = Available, P= Preferred, U = Unavailable): ")
        for day in range(1,32):
            caregivers[name]["availability"][day] = {
                "AM": input(f"Day {day} - AM shift (A/U/P): ").strip().upper(),
                "PM": input(f"Day {day} - PM shift (A/U/P): ").strip().upper(),

            }

    return caregivers


#test


if __name__ == "__main__":
    caregivers= input_caregiver_details()
    for name, details in caregivers.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}\n")
