
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

#class for caregivers

class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.availability = {}  # availability will be stored by day
        self.assigned_hours = 0  # total assigned hours for the caregiver

    def set_availability(self):
        """ask user to enter availability for each day of the month"""
        print(f"\nSet availability for {self.name} (A = Available, P = Preferred, U = Unavailable):")
        for day in range(1, 32):  # days 1 to 31
            # new logic for getting availability, this will handle invalid input
            while True:
                am_shift = input(f"Day {day} - AM shift (A/U/P):").strip().upper()
                if am_shift in ["A", "U", "P"]:
                    break # if its valid it exits this little mini loop
                print("Please enter A, U, or P")
            while True:
                pm_shift = input(f"Day {day} - PM shift (A/U/P):").strip().upper()
                if pm_shift in ["A", "U", "P"]:
                    break
                print("Please enter A, U, or P")
            # save availability for the day
            self.availability[day] = {"AM": am_shift, "PM": pm_shift} 

    def __str__(self):
        """I want it to return a string fr the caregiver """
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Pay Rate: ${self.pay_rate:.2f}"





# 
# Schedule Manager class for assigning and displaying schedules
class ScheduleManager:
    def __init__(self, caregivers, year, month):
        self.caregivers = caregivers
        self.year = year #the sch year
        self.month = month #the sch month
        self.schedule = {}  # empty dictionary for the schedule

    def assign_shifts(self):
        """assigns shifts to caregivers based on their availability and preference"""
        shifts = ["7:00am - 1:00pm", "1:00pm - 7:00pm"]
        num_days = calendar.monthrange(self.year, self.month)[1]

        for day in range(1, num_days + 1):
            self.schedule[day] = {}  # dictionary for this day's shifts
            for shift in shifts:
                shift_type = "AM" if shift == shifts[0] else "PM"  # AM or PM shift
                # caregivers who preferred the shift first
                preferred = [cg for cg in self.caregivers if cg.availability.get(day, {}).get(shift_type) == "P"]
                # caregivers who are available
                available = [cg for cg in self.caregivers if cg.availability.get(day, {}).get(shift_type) == "A"]

                if preferred:
                    assigned = preferred[0]  # the first person in the preferred list is assigned
                elif available:
                    assigned = available[0]
                else:
                    assigned = None  # unassigned if no one is available

                # Assign caregiver or mark as "Unassigned"
                self.schedule[day][shift] = assigned.name if assigned else "Unassigned"

                # If the shift is assigned, add to the caregiver's hours
                if assigned:
                    assigned.assigned_hours += shift_hours

    def display_schedule_as_html(self):
        """
        Generates an HTML file for the comprehensive work schedule.
        """
        html_schedule = f"""
        <html>
        <head>
            <title>Work Schedule for {calendar.month_name[self.month]} {self.year}</title>
            <style>
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid black; padding: 10px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Work Schedule for {calendar.month_name[self.month]} {self.year}</h1>
            <table>
                <tr>
                    <th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th>
                </tr>
        """
        # get the first weekday of the month and the total days
        first_weekday, num_days = calendar.monthrange(self.year, self.month)
        current_day = 1

        for week in range((num_days + first_weekday) // 7 + 1):  # Loop through weeks
            html_schedule += "<tr>"
            for day in range(7):  # loop through days of the week
                if (week == 0 and day < first_weekday) or current_day > num_days:
                    html_schedule += "<td></td>"  # empty cell for days outside the month
                else:
                    # add the day and the assigned shifts
                    shifts_for_day = self.schedule[current_day]
                    am_shift = shifts_for_day.get("7:00am - 1:00pm", "N/A")
                    pm_shift = shifts_for_day.get("1:00pm - 7:00pm", "N/A")
                    html_schedule += f"<td>{current_day}<br><b>AM:</b> {am_shift}<br><b>PM:</b> {pm_shift}</td>"
                    current_day += 1
            html_schedule += "</tr>"

        html_schedule += "</table></body></html>"
        # added part to the dempwolf ex so it can pop up in browser
        file_name = f"work_schedule_{self.year}_{self.month}.html"
        with open(file_name, "w") as file:
            file.write(html_schedule)
        webbrowser.open(f"file://{os.path.abspath(file_name)}")



# 
# availability Manager class for generating individual caregiver schedules
class AvailabilityManager:
    def __init__(self, caregiver, year, month):
        self.caregiver = caregiver
        self.year = year
        self.month = month

    def generate_availability_schedule(self):
        """
        Generates an HTML file summarizing the caregiver's availability.
        """
        html = f"""
        <html>
        <head>
            <title>{self.caregiver.name}'s Availability for {calendar.month_name[self.month]} {self.year}</title>
            <style>
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid black; padding: 10px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>{self.caregiver.name}'s Availability for {calendar.month_name[self.month]} {self.year}</h1>
            <table>
                <tr><th>Day</th><th>AM</th><th>PM</th></tr>
        """
        for day in range(1, calendar.monthrange(self.year, self.month)[1] + 1):
            am = self.caregiver.availability.get(day, {}).get("AM", "Unavailable")
            pm = self.caregiver.availability.get(day, {}).get("PM", "Unavailable")
            html += f"<tr><td>{day}</td><td>{am}</td><td>{pm}</td></tr>"

        html += "</table></body></html>"
        # will pop up in browser
        file_name = f"availability_schedule_{self.caregiver.name}.html"
        with open(file_name, "w") as file:
            file.write(html)
        webbrowser.open(f"file://{os.path.abspath(file_name)}")



# Salary calculation
class SalaryCalculator:
    def __init__(self, caregivers):
        self.caregivers = caregivers

    def calculate_salary_report(self):
        """calculates and makes a salary report for all caregivers"""
        salary_report = []  # empty now but will store report lines
        total_monthly_pay = 0

        for caregiver in self.caregivers:
            hours = caregiver.assigned_hours  # the hours assigned to this caregiver
            total_pay = hours * caregiver.pay_rate  # the pay for this caregiver
            salary_report.append(f"Caregiver: {caregiver.name}, Total Hours: {hours}, Total Pay: ${total_pay:.2f}")
            total_monthly_pay += total_pay  # adds to the pay

        salary_report.append(f"\nTotal Monthly Pay: ${total_monthly_pay:.2f}")

        # save to txt
        with open("salary_report.txt", "w") as file:
            file.write("\n".join(salary_report))

        print("Salary report generated and saved as salary_report.txt")


# Main Function
if __name__ == "__main__":
    #main func for collect caregiver details
    num_caregivers = int(input("Enter the number of caregivers: "))
    caregivers = []
    for _ in range(num_caregivers):
        name = input("Enter caregiver's name: ")
        phone = input(f"Enter {name}'s phone number: ")
        email = input(f"Enter {name}'s email: ")
        pay_rate = float(input(f"Enter {name}'s hourly pay rate (0 if unpaid): "))
        caregiver = Caregiver(name, phone, email, pay_rate)
        caregiver.set_availability()
        caregivers.append(caregiver)

    # assign shifts and generate comprehensive schedule
    year = int(input("Enter the year for the schedule: "))
    month = int(input("Enter the month (1-12) for the schedule: "))
    schedule_manager = ScheduleManager(caregivers, year, month)
    schedule_manager.assign_shifts()
    schedule_manager.display_schedule_as_html()

    # need individual availability schedules
    for caregiver in caregivers:
        availability_manager = AvailabilityManager(caregiver, year, month)
        availability_manager.generate_availability_schedule()

    #Calculate salaries and generate salary report
    salary_calculator = SalaryCalculator(caregivers)

    salary_calculator.calculate_salary_report()
