day=int(input("enter the day(1-31)"))
month=int(input("enter the month(1-12)"))
year=int(input("enter the year(2018)"))
print(f"enter the date:{day:02d}-{month:02d}-{year}")
if(year % 4==0 and year % 100 !=0) or (year % 400==0):
    print(f"the year{year} is leap year")
else:
    print(f"the year {year} is not leap year")
