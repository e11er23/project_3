#Project 3 python file

print("test")
import calendar
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

shift_hours = 6 # 7-1 and 1-7 are both 6 hour shifts

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

# REMEMBER TO ADD SOMETHING TO HANDLE IF THEY ENTER SOMETHING OTHER THAN A,U,P
#test


# if __name__ == "__main__":
#     caregivers= input_caregiver_details()
#     for name, details in caregivers.items():
#             print(f"Name: {name}")
#             print(f"Phone: {details['phone']}")
#             print(f"Email: {details['email']}\n")


#assign people shifts
# part of this code is from the class sample code, and part is tweaked
def assign_shifts(caregivers, year, month):
    shifts = ["7:00AM - 1:00PM", "1:00PM - 7:00PM"]

    num_days= calendar.monthrange(year,month)[1] #gets the number of days for the month

    schedule = {} #empty to begin

    for day in range(1, num_days + 1):
        schedule[day] = {} #dic for this days shifts

        for shift in shifts:
            shift_type = "AM" if shift== shifts[0] else "PM" #if the shift is whats first in the shifts list it will be am but if not it will be PM



            #want the people who preferred the shift
            preferred = [ name for name, details in caregivers.items() if details["availability"][day][shift_type]== "P"] # will get the ones that are preferred

            #available 
            available = [ name for name, details in caregivers.items() if details["availability"][day][shift_type]== "A"] # will get the ones that are available

            
                         
            if preferred:
                assigned = preferred[0] #the first person in the preffered list is assigned
            elif available:
                assigned = available[0]
            else:
                assigned = "unassigned"

            schedule[day][shift]= assigned

            if assigned != "unassigned":
                caregivers[assigned]["assigned_hours"] += shift_hours #if the shift is assigned it will add to the hours

    return schedule 

#test
# def test_assign_shifts(caregivers):
#     year= 2024
#     month= 11

#     schedule = assign_shifts(caregivers, year, month)

#     print("\nschedule:")
#     for day, shifts in schedule.items():
#         print(f"Day {day}:")
#         for shift, assigned in shifts.items():
#             print(f"{shift}: {assigned}")

#     print("\nCaregiver assigned hours:")
#     for name, details in caregivers.items():
#         print(f"{name}: {details['assigned_hours']} hours")


# if __name__ == "__main__":
#     print("Enter caregiver details...\n")
#     caregivers = input_caregiver_details()


#     test_assign_shifts(caregivers)
