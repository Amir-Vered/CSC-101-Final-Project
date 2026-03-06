import datetime
from Reading import Reading


class City:
    def __init__(self, path:str, test_day:int, test_week:int, test_month:int):
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
        self.monthly_average = self.average_monthly(test_month)
        self.weekly_average = self.average_weekly(test_week)
        self.daily_average = self.average_daily(test_day)
        self.highest_value = self.highest_recording()
        self.lowest_value = self.lowest_recording()
        self.days_exceeding_WHO = self.days_exeeding_health_standards(5) # WHO: 5 ug/m^3
        self.days_exceeding_EPA = self.days_exeeding_health_standards(9) # EPA: 9 ug/m^3
        self.days_exceeding_EPA_24hr = self.days_exeeding_health_standards(35) # EPA 24 Hr: 35 ug/m^3

        print(self.monthly_average)
        print(self.daily_average)
        print(self.weekly_average)
        print(self.highest_value)
        print(self.lowest_value)
        print(len(self.days_exceeding_WHO))
        print(len(self.days_exceeding_EPA))
        print(len(self.days_exceeding_EPA_24hr))

    def average_monthly(self, month:int) -> float:
        l = []
        for r in self.readings:
            if r.month == month:
                l.append(r)
        sum = 0
        for r in l:
            sum += r.value
        return sum / len(l)

    def average_weekly(self, week:int) -> float:
        l = []
        for r in self.readings:
            if datetime.date(r.year, r.month, r.day).isocalendar().week == week:
                l.append(r)
        sum = 0
        for r in l:
            sum += r.value
        return sum / len(l)

    def average_daily(self, day:int) -> float:
        l = []
        for r in self.readings:
            if datetime.date(r.year, r.month, r.day).timetuple().tm_yday == day:
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

    def days_exeeding_health_standards(self, value:float) -> list[list[Reading]]:
        return [r for r in self.readings if r.value > value]