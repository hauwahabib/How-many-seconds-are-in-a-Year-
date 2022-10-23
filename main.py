print("How many seconds are in a year Calculator")
print()
secsInMinute = int(input("How many seconds in a minutes?"))
minsInHour = int(input("How many minutes in an hour?"))
hoursInDay = int(input("How many hours in a day?"))
minsInDay2 = secsInMinute * hoursInDay 
DaysInYear = int(input("How many days are in year?"))
DaysInLeapYear = 366
leapyearAnswer = DaysInLeapYear * hoursInDay * minsInHour * secsInMinute 
if DaysInYear == 365 :
  MinsInYear = DaysInYear * 1440 
  answer = secsInMinute * MinsInYear 
  print()
  print("There are", answer, "in a year")
else :
  print("There are", leapyearAnswer, "in a leap year")


  
  