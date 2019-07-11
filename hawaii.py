import datetime
import math
def solution(Y, A, B, W):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = FORTH = 3  # for people who have finger trouble
    FIFTH = 4
    LAST = -1
    SECONDLAST = -2
    THIRDLAST = -3

    MONDAY = MON = 0
    TUESDAY = TUE = TUES = 1
    WEDNESDAY = WED = 2
    THURSDAY = THU = THUR = 3
    FRIDAY = FRI = 4
    SATURDAY = SAT = 5
    SUNDAY = SUN = 6
    
    month =1
    if A == 'January':
            monthA = 1
    elif A == 'February':
        monthA = 2
    elif A == 'March':
        monthA = 3
    elif A == 'April':
        monthA = 4
    elif A == 'May':
        monthA = 5
    elif A == 'June':
        monthA = 6
    elif A == 'July':
        monthA = 7
    elif A == 'August':
        monthA = 8
    elif A == 'September':
        monthA = 9
    elif A == 'October':
        monthA = 10
    elif A == 'November':
        monthA = 11
    elif A == 'December':
        monthA = 12

    if B == 'January':
        monthB = 1
    elif B == 'February':
        monthB = 2
    elif B == 'March':
        monthB = 3
    elif B == 'April':
        monthB = 4
    elif B == 'May':
        monthB = 5
    elif B == 'June':
        monthB = 6
    elif B == 'July':
        monthB = 7
    elif B == 'august':
        monthB = 8
    elif B == 'September':
        monthB = 9
    elif B == 'October':
        monthB = 10
    elif B == 'November':
        monthB = 11
    elif B == 'December':
        monthB = 12
    
    FEBRUARY = FEB = 2
    MARCH = MAR = 3
    APRIL = APR = 4
    MAY = 5
    JUNE = JUN = 6
    JULY = JUL = 7
    AUGUST = AUG = 8
    SEPTEMBER = SEP = 9
    OCTOBER = OCT = 10
    NOVEMBER = NOV = 11
    DECEMBER = DEC = 12
    
    def dow_date_finder(which_weekday_in_month,day,month,year):
        dt = datetime.date(year,month,1)
        dow_lst = []
        while dt.weekday() != day:
            dt = dt + datetime.timedelta(days=1)
        while dt.month == month:
            dow_lst.append(dt)
            dt = dt + datetime.timedelta(days=7)
        return dow_lst[which_weekday_in_month]
    
    start_date = dow_date_finder(FIRST,MONDAY,monthA,Y)
    end_date = dow_date_finder(LAST,SUNDAY,monthB,Y)
    date_delta = end_date - start_date
    result = math.ceil(date_delta.days/7)
    return result


print(solution(2014,'April','May','Wednesday'))