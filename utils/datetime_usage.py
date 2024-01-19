from datetime import datetime

date_string = '21 June, 2018'

# 1.Get Current Date and Time
# datetime_object = datetime.now()
# print("now time is = ", datetime_object)

# 2.Get Current Date
# date_object = datetime
# print("Current Date is = ", date_object)
# https://www.programiz.com/python-programming/datetime

# n
# print("date string =", date_string)
# print("type of date string =", type(date_string))
#
# date_object_2 = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object = ", date_object_2)


format_now_day = datetime.now().strftime("%Y%m%d")
now_day = datetime.now().strftime("%Y-%m-%d")
print(now_day)

nowHour = datetime.now().strftime("%H")
print(nowHour)

format_datatime_now = datetime.now().strftime("%Y%m%d %H:%M:%S")
print(format_datatime_now)
