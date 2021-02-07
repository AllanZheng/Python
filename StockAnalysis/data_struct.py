class stockdata:
    Weekday = 1
    IsIncrease = True
    Code = ''
    Name = ''
    Date = ''

    def __init__(self, a, b, c, d, date):
        self.Weekday = a
        self.IsIncrease = b
        self.Code = c
        self.Name = d
        self.Date = date