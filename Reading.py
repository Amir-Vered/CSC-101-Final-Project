class Reading:
    def __init__(self, month:int, day:int, year:int, hour:int, minute:int, value:float):
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute
        self.value = value

    def __repr__(self):
        return "{} ug/m^3 -- {}/{}/{}, {}:{}".format(self.value, self.month, self.day, self.year, self.hour, str(self.minute).zfill(2))