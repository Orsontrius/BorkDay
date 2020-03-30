import datetime

dogYear = datetime.timedelta(days=52.143)

month = int(input("Please enter your dogs birthmonth (ex. May  = 5)\n"))
day = int(input("Please enter your dogs birthday\n"))

borkDay = datetime.datetime(2020, month, day)

print("\nHere are your dog's birthdays for the next human year")
for x in range(8):
    print(borkDay.date())
    borkDay = borkDay + dogYear
