year=int(input("Input a year:"))
month=int(input("Input a month[1-12]:"))
day=int(input("Input a day[1-31]:"))
day_uvelichenie=day+1
next_date=[]
if day<1 or day>31 and month<1 or month>12:
    print("Error!!!")
else:
    if day==31 and month==12:
        year=year+1
        month=1
        day=1
        next_date.append(year)
        next_date.append(month)
        next_date.append(day)
        print("The next date is[yyyy,mm,dd]:",next_date)
    elif month==4 or 6 or 9 or 11 and day==30:
        month=month+1
        day=1
        next_date.append(year)
        next_date.append(month)
        next_date.append(day)
        print("The next date is[yyyy,mm,dd]:",next_date)
    elif month==2 and day==28:
        month=month+1
        day=1
        next_date.append(year)
        next_date.append(month)
        next_date.append(day)
        print("The next date is[yyyy,mm,dd]:",next_date)
    elif month==1 or 3 or 5 or 7 or 8 or 10 and day==31:
        month=month+1
        day=1
        next_date.append(year)
        next_date.append(month)
        next_date.append(day)
        print("The next date is[yyyy,mm,dd]:",next_date)

    else:
        next_date.append(year)
        next_date.append(month)
        next_date.append(day_uvelichenie)
        print("The next date is[yyyy,mm,dd]:",next_date)

    



