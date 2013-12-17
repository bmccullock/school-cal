from calendar import Calendar, day_name, month_name
import itertools

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

    def __init__(self, school_days):
        self.days = []
        for day in school_days:
            self.days.append(SchoolDay(*day))

    def __repr__(self):
        return '<SchoolYear containing %d SchoolDay objects>' % len(self.days)

    def get_month(self, year, month):
        day_set = []
        for d in self.days:
            if d.month == month:
                day_set.append(d)
        return day_set

    def get_rotation_days(self, rotation_number):
        day_set = []
        for d in self.days:
            if d.rotation == rotation_number:
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
        if self.day == 1:
            return True
        else:
            return False


def build_calendar(calendar, MONTHS, HOLIDAYS):
    '''Build a list of school days and remove any holidays'''
    school_days = []
    for m in MONTHS:
        date_gen = calendar.itermonthdays2(m[0], m[1])
        for d in date_gen:
            if (d[0] > 0) and (d[1] < 5):
                val = [m[0], m[1], d[0], d[1]] # year, month, date, day, (rotation)
                school_days.append(val)
    # Check the list of holidays and remove from the list
    for month in HOLIDAYS.iterkeys():
        values = HOLIDAYS.get(month)
        for v in values:
            for d in school_days:
                if (d[1] == month) and (d[2] == v):
                    school_days.remove(d)   
    # create a generator for the rotation schedule and append the rotation day to each day
    # adjust the [start] parameter of islice to start from diff rotation day
    rotation = itertools.islice( (itertools.cycle([i for i in range(1, 7)]) ), 0, None)
    for date in school_days:
        date.append(rotation.next())
    return school_days

if __name__ == '__main__':
    school_cal = SchoolYear( build_calendar(Calendar(), MONTHS, HOLIDAYS) )
    for d in school_cal.get_month(2014, 3):
        print d



