#!/usr/bin/env python3

# sundays


def days_in_month(month, year, thirty=[9, 4, 6, 11]):
    if month in thirty:
        return 30
    if month == 2:
        if year % 400 == 0:
            return 29
        if year % 100 == 0:
            return 28
        if year % 4 == 0:
            return 29
        return 28
    return 31


def next_day(day, month, year):
    max_day = days_in_month(month, year)

    if day < max_day:
        return day + 1, month, year
    if month < 12:
        return 1, month + 1, year
    return 1, 1, year + 1


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", 'September', 'October', 'November', 'December']

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def go():
    day, month, year = 1, 1, 1900
    week_day = 0  # monday

    count = 0  # sundays on the first of the month
    while True:
        day, month, year = next_day(day, month, year)
        week_day = (week_day + 1) % 7
#        print(day, months[month - 1], year, weekdays[week_day])

        if year == 2001:
            break

        if year >= 1901 and day == 1 and week_day == 6:

            count += 1

    print(count)
