import datetime
import calendar
def meetup_day(year, month, day_of_the_week, which):
    which_lookup = {"1st": 1, "2nd": 8, "3rd": 15, "4th": 22, "5th": 29, "last" : -1, "teenth" : 13}
    day_lookup = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    day_val = day_lookup[day_of_the_week]
    val = which_lookup[which]

    if (val == -1):
        d = datetime.date(year,month, calendar.monthrange(year,month)[1])
        day_delta = d.weekday()-day_val
        if day_delta < 0:
            day_delta += 7
        return d -datetime.timedelta(day_delta)

    d = datetime.date(year,month,val)
    day_delta = day_val-d.weekday()
    if day_delta < 0:
        day_delta += 7
    return d + datetime.timedelta(day_delta)

