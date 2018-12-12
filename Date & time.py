from datetime import date, timedelta, datetime
import locale
locale.setlocale(locale.LC_ALL, "russian")
today = date.today()
today_output = today.strftime('%A %d %B %Y')
print ("Сегодня: {}".format(today_output))

delta = timedelta(days=1)
yesterday = today - delta
yesterday_output = yesterday.strftime('%A %d %B %Y')
print ("Вчерашняя дата: {}".format(yesterday_output))

month_delta = timedelta(days=30)
month_back = today - month_delta
month_back_output = month_back.strftime('%A %d %B %Y')
print ("Месяц назад было: {}".format(month_back_output))

Input_string = "01/01/17 12:10:03.234567"
normal_time = datetime.strptime(Input_string,"%d/%m/%y %H:%M:%S.%f")
print ("Строка: {}".format(normal_time))