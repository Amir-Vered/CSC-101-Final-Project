import datetime
from Reading import Reading
import sys


class City:
    def __init__(self, path:str, date:str):
        self.name = path.removesuffix(".csv")
        self.date = date

        r = []
        with open("./data/" + path, "r", encoding="utf-8", newline="") as f:
            lines = f.read().splitlines()
        for i in range(1, len(lines)):
            l = lines[i].split(',')
            t = l[0].split(' ')
            d = t[0].split('/')
            c = t[1].split(':')

            try:
                r.append(Reading(int(d[0]), int(d[1]), int(d[2]), int(c[0]), int(c[1]), float(l[1])))
            except:
                print("Data Parsing Error on Line", i)

        self.readings = r

        try:
            dt = datetime.date(int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1]))
            self.month = dt.month
            self.week = dt.isocalendar().week
            self.day = dt.timetuple().tm_yday
            self.monthly_average = self.average_monthly(self.month, dt.year)
            self.weekly_average = self.average_weekly(self.week, dt.year)
            self.daily_average = self.average_daily(self.day, dt.year)
        except:
            print("Date improperly formated or out of bounds")
            sys.exit(1)

        self.highest_value = self.highest_recording()
        self.lowest_value = self.lowest_recording()
        self.readings_exceeding_WHO = self.readings_exeeding_health_standards(5.0) # WHO: 5.0 ug/m^3
        self.readings_exceeding_EPA = self.readings_exeeding_health_standards(9.0) # EPA: 9.0 ug/m^3
        self.readings_exceeding_EPA_24hr = self.readings_exeeding_health_standards(35.0) # EPA 24 Hr: 35.0 ug/m^3

    def __repr__(self):
        return '''
----------  {}  ----------
Averages from {}:
 Monthly Average For Month of {}: 
     {} ug/m^3
 Weekly Average For Week of {}: 
     {} ug/m^3
 Daily Average For {}: 
     {} ug/m^3

Complete Dataset:
 Highest Value Recorded: 
     {}
 Lowest Value Recorded:
     {}
 Readings Exceeding WHO Standards (5.0 ug/m^3):
     {}
 Readings Exceeding EPA Standards (9.0 ug/m^3):
     {}
 Readings Exceeding EPA 24hr Standards (35.0 ug/m^3):
     {}'''.format(self.name,
                 self.date,
                 self.date,
                 round(self.monthly_average, 3),
                 self.date,
                 round(self.weekly_average, 3),
                 self.date,
                 round(self.daily_average, 3),
                 self.highest_value,
                 self.lowest_value,
                 len(self.readings_exceeding_WHO),
                 len(self.readings_exceeding_EPA),
                 len(self.readings_exceeding_EPA_24hr))

    def average_monthly(self, month:int, year:int) -> float:
        l = []
        for r in self.readings:
            if r.month == month and r.year == year:
                l.append(r)
        sum = 0
        for r in l:
            sum += r.value
        return sum / len(l)

    def average_weekly(self, week:int, year:int) -> float:
        l = []
        for r in self.readings:
            if datetime.date(r.year, r.month, r.day).isocalendar().week == week and r.year == year:
                l.append(r)
        sum = 0
        for r in l:
            sum += r.value
        return sum / len(l)

    def average_daily(self, day:int, year:int) -> float:
        l = []
        for r in self.readings:
            if datetime.date(r.year, r.month, r.day).timetuple().tm_yday == day and r.year == year:
                l.append(r)
        sum = 0
        for r in l:
            sum += r.value
        return sum / len(l)

    def highest_recording(self) -> Reading:
        maxi = 0
        for i in range(1, len(self.readings)):
            if self.readings[i].value > self.readings[maxi].value:
                maxi = i
        return self.readings[maxi]

    def lowest_recording(self) -> Reading:
        mini = 0
        for i in range(1, len(self.readings)):
            if self.readings[i].value < self.readings[mini].value:
                mini = i
        return self.readings[mini]

    def readings_exeeding_health_standards(self, value:float) -> list[list[Reading]]:
        return [r for r in self.readings if r.value > value]