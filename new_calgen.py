from calendar import Calendar, day_name, month_name, TextCalendar
import itertools

# Must be a way to do this better
MONTHS = ((2013, 9), (2013, 10), (2013, 11), (2013, 12), (2014, 1), (2014, 2), (2014, 3), 
    (2014, 4), (2014, 5), (2014, 6))

HOLIDAYS = {
    9: [2, 5],
    10: [14],  
    11: [11, 28, 29],  
    12: [23, 24, 25, 26, 27, 30, 31],
    1: [1, 20],
    2: [17, 18, 19, 20, 21],
    3: [],
    4: [18, 21, 22, 23, 24, 25],
    5: [26],
    6: [26, 27, 30]
}

class SchoolYear:
    '''Collection of school days'''

    def __init__(self, calendar, MONTHS, HOLIDAYS, rotation_start):
        self.days = []

        # Build a list of school days and remove any holidays. Return as a list with
        # each day represented as: [year, month, date, day, rotation]  
        # rotation_start = the rotation number for the first day of school
        temp_days = []
        for m in MONTHS:
            for d in calendar.itermonthdays2(m[0], m[1]): # year, month
                if (d[0] > 0) and (d[1] < 5): # date not null (0) and day not sat/sun 
                    val = [m[0], m[1], d[0], d[1]] # year, month, date, day
                    temp_days.append(val)
        # Remove any holidays
        for month in HOLIDAYS.iterkeys():
            for date in HOLIDAYS.get(month):
                for d in temp_days:
                    if (d[1] == month) and (d[2] == date):
                        temp_days.remove(d) 
        # create a generator for the rotation schedule and append the rotation day to each day
        start = rotation_start - 1
        rotation = itertools.islice( (itertools.cycle( [i for i in range(1, 7)]) ), start, None)
        for date in temp_days:
            date.append(rotation.next())

        for day in temp_days:
            self.days.append(SchoolDay(*day))

    def __repr__(self):
        return '<SchoolYear containing %d SchoolDay objects>' % len(self.days)

    def get_month(self, year, month):
        # return list of all SchoolDay objects in the given month
        day_set = []
        for d in self.days:
            if d.month == month:
                day_set.append(d)
        return day_set

    def get_rotation_days(self, rotation_number):
        # return list of all SchoolDay objects matching rotation_number
        day_set = []
        for d in self.days:
            for each in rotation_number:  
                if d.rotation == each:
                    day_set.append(d)
        return day_set


class SchoolDay(object):
    '''A single school day'''

    def __init__(self, year, month, date, day, rotation):
        self.year = year
        self. month = month
        self.date = date
        self.day = day
        self.rotation = rotation

    def __str__(self):
        return '%s/%s/%s, %s (Day %s)' % (self.month, self.date, self.year, day_name[self.day], self.rotation)

    def is_tuesday(self):
        # Check if the SchoolDay is a Tuesday
        if self.day == 1:
            return True
        else:
            return False



if __name__ == '__main__':
    school_cal = SchoolYear( Calendar(), MONTHS, HOLIDAYS, 1 )
    for d in school_cal.get_rotation_days([1, 2, 3, 6]):
        print d




