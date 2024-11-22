#Project 3 python file

print("test")
import calendar
import webbrowser
import os
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
#new logic for getting avail, this will handle if there isnt an input that will 
            while True:
                am_shift = input(f"Day {day} - AM shift (A/U/P):").strip().upper()
                if am_shift in ['A', 'U', 'P']:
                    break # if its valid it exits this little mini loop
                print('Please enter A, U, or P')

            while True:
                pm_shift = input(f"Day {day} - AM shift (A/U/P):").strip().upper()
                if pm_shift in ['A', 'U', 'P']:
                    break
                print("Enter A,U, or P")

            #need to save avail for the day
            caregivers[name]['availability'][day]= {"AM": am_shift, "PM": pm_shift}

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
            preferred = [
                name for name, details in caregivers.items()
                if details["availability"].get(day, {}).get(shift_type) == "P"
            ]
            #available 
            available = [
                name for name, details in caregivers.items()
                if details["availability"].get(day, {}).get(shift_type) == "A"
            ]
            
                         
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

#html part work schedule, taken from "Sample care calendar" that prof demp gave us
def display_schedule_as_html(schedule, year, month):
    # Create the HTML structure
    html_schedule = f"""
    <html>
    <head>
        <title>Work Schedule for {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            td {{
                height: 100px;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        <h1>Work Schedule for {calendar.month_name[month]} {year}</h1>
        <table>
            <tr>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
    """
    
    # Get the first weekday of the month and the total days
    first_weekday, num_days = calendar.monthrange(year, month)

    # Fill in the days of the month
    current_day = 1
    for week in range((num_days + first_weekday) // 7 + 1):
        html_schedule += "<tr>"
        for day in range(7):
            if (week == 0 and day < first_weekday) or current_day > num_days:
                html_schedule += "<td></td>"  # Empty cell for days outside the month
            else:
                # Add the day and the assigned shifts
                shifts_for_day = schedule.get(current_day, {})
                morning_shift = shifts_for_day.get("7:00AM - 1:00PM", "N/A")
                afternoon_shift = shifts_for_day.get("1:00PM - 7:00PM", "N/A")

                html_schedule += f"<td>{current_day}<br><b>AM:</b> {morning_shift}<br><b>PM:</b> {afternoon_shift}</td>"
                current_day += 1
        html_schedule += "</tr>"

    # Close the table and HTML
    html_schedule += """
        </table>
    </body>
    </html>
    """
    

#This part is different from prof demp's sample because I want it to open in chrome


# Save the HTML file
    file_name = f"work_schedule_{year}_{month}.html"
    file_path = os.path.abspath(file_name)
    with open(file_name, "w") as file:
        file.write(html_schedule)

    # Print confirmation with the correct file name
    print(f"Work schedule saved as {file_path}")

    # Open the file in the default web browser
    webbrowser.open(f"file://{file_path}", new=2)







######################## html avail schedule created using AI as allowed by proj directions
def generate_availability_schedule(caregiver_name, details, year, month):
    """
    Generates an HTML table summarizing caregiver's availability.
    """
    # Start the HTML for the caregiver's availability
    html = f"""
    <html>
    <head>
        <title>{caregiver_name}'s Availability for {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>{caregiver_name}'s Availability for {calendar.month_name[month]} {year}</h1>
        <table>
            <tr>
                <th>Day</th>
                <th>AM</th>
                <th>PM</th>
            </tr>
    """

    # Add rows for each day in the month
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        am = details["availability"].get(day, {}).get("AM", "Unavailable")
        pm = details["availability"].get(day, {}).get("PM", "Unavailable")
        html += f"<tr><td>{day}</td><td>{am}</td><td>{pm}</td></tr>"

    # Close the HTML structure
    html += """
        </table>
    </body>
    </html>
    """

    # Save the HTML to a file
    file_name = f"availability_schedule_{caregiver_name}.html"
    file_path = os.path.abspath(file_name)
    with open(file_name, "w") as file:
        file.write(html)

    # Print confirmation and open the file
    print(f"Availability schedule saved as {file_path}")
    webbrowser.open(f"file://{file_path}", new=2) 
    ##########
    
    #test
if __name__ == "__main__":
    
    print("Enter caregiver details...\n")
    caregivers = input_caregiver_details()

    
    while True:
        try:
            year = int(input("Enter the year for the schedule (e.g., 2024): "))
            if year > 0:  # make sure year is a positive number
                break
            else:
                print("Year must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid year as a number (ex 2024).")

    while True:
        month = int(input("Enter the month (1-12) for the schedule: "))
        if 1 <= month <= 12:  # Check if month is within valid range
                break
        else:
            print("Month must be a number between 1 and 12. Try again.")


    #avail schedule for each
    for name, details in caregivers.items():
        generate_availability_schedule(name, details, year, month)
    #comp schedule


 #avail schedule for each
    for name, details in caregivers.items():
        generate_availability_schedule(name, details, year, month)
 #comp schedule

    schedule = assign_shifts(caregivers, year, month)

    
    display_schedule_as_html(schedule, year, month)


