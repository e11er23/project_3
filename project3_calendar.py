# %%
# project 03 file
# calendar code
# used from sample given



import calendar
import random



# creating schedule using the sample given
def make_schedule(caregivers, year, month):
    # creating the two shifts per day between AM and PM
    shifts = ['7:00am - 1:00pm', '1:00pm - 7:00pm']
    # shows the days within the month
    num_days = calendar.monthrange(year, month)[1]
    # creates dictionary for the schedule
    schedule = {}

    # loops each day of the month
    for day in range(1, num_days + 1):
        # creates schedule for each day
        schedule[day] = {}
        for shift in shifts:
            # shows each caregiver and thier preferred or available shifts
            # code for those who are available
            available_caregivers = [
                name for name, details in caregivers.items()
                if details['availability'][day][shift.split()[0]] in ['A', 'P']
            ]
            
            # allowing the schedule to be shuffled based on their availability
            random.shuffle(available_caregivers)

            # code for those who are marked as prefered
            preferred_caregivers = [
                name for name in available_caregivers
                if caregivers[name]['availability'][day][shift.split()[0]] == 'P'
            ]
            
            # assigned preferred caregivers based on availability
            # if not preferred, assigned shifts on general availability
            # marked unassigned if no caregivers available
            if preferred_caregivers:
                assigned = preferred_caregivers[0]
            elif available_caregivers:
                assigned = available_caregivers[0]
            else:
                assigned = 'Unassigned'
            
            schedule[day][shift] = assigned

    return schedule



# creating HTML calendar
# using sample
def html_calendar(schedule, year, month):
    html = f"""
    <html>
    <head>
        <title>Schedule for {calendar.month_name[month]} {year}</title>
        <style>
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid black; padding: 5px; text-align: center; }}
            th {{ background-color: #f0f0f0; }}
        </style>
    </head>
    <body>
        <h1>Schedule for {calendar.month_name[month]} {year}</h1>
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

    # start from the beginning of the week and all days within the month
    first_weekday, num_days = calendar.monthrange(year, month)
    # starting with the first day of the month
    current_day = 1

    for week in range((num_days + first_weekday) // 7 + 1):
        html += '<tr>'

        # loops through 7 days a week
        for day in range(7):
            if (week == 0 and day < first_weekday) or current_day > num_days:
                html += '<td></td>'
            else:
                # show assigned caregivers
                morning = schedule[current_day].get('7:00am - 1:00pm', 'N/A')
                afternoon = schedule[current_day].get('1:00pm - 7:00pm', 'N/A')

                # assigning them to the cells
                html += f"<td>{current_day}<br><b>7:00am-1:00pm:</b> {morning}<br><b>1:00pm-7:00pm:</b> {afternoon}</td>"
                current_day += 1

        html += '</tr>'
    html += '</table></body></html>'

    # saving HTML to file
    with open(f'schedule_{year}_{month}.html', 'w') as file:
        file.write(html)

    print(f'HTML schedule for {calendar.month_name[month]} {year} has been saved.')



# creating caregivers dictionary
if __name__ == '__main__':
    # input different caregivers and thier preference and availability
    caregivers = {
        'Josh': {'availability': {day: {'7:00am': 'A', '1:00pm': 'P'} for day in range(1, 32)}},
        'Ryan': {'availability': {day: {'7:00am': 'U', '1:00pm': 'P'} for day in range(1, 32)}},
        'Layan': {'availability': {day: {'7:00am': 'A', '1:00pm': 'P'} for day in range(1, 32)}},
        'Sam': {'availability': {day: {'7:00am': 'P', '1:00pm': 'A'} for day in range(1, 32)}},
        'Mia': {'availability': {day: {'7:00am': 'A', '1:00pm': 'A'} for day in range(1, 32)}},
        'Liam': {'availability': {day: {'7:00am': 'P', '1:00pm': 'U'} for day in range(1, 32)}},
        'Ava': {'availability': {day: {'7:00am': 'P', '1:00pm': 'A'} for day in range(1, 32)}},
        'James': {'availability': {day: {'7:00am': 'U', '1:00pm': 'P'} for day in range(1, 32)}}
    }
    # 8 caregivers and their preference, availability, and unavailability^

    year = int(input('Enter the year: '))
    month = int(input('Enter the month (1-12): '))
    schedule = make_schedule(caregivers, year, month)
    html_calendar(schedule, year, month)