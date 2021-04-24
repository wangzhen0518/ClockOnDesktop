import time

NowTime = time.localtime((time.time()))
print("Year: " + str(NowTime[0]), end="  ")
print("Month: " + str(NowTime[1]), end="  ")
print("Date: " + str(NowTime[2]), end="  ")
print("Hour: " + str(NowTime[3]), end="  ")
print("Minute: " + str(NowTime[4]), end="  ")
print("Second: " + str(NowTime[5]), end="  ")
print("WeekDay: " + str(NowTime[6]), end="\n")
print("YearDay: " + str(NowTime[7]))
