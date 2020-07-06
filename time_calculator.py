def add_time(start, duration , day=None):
  day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  start_time = start.split(":")
  start_hour = int(start_time[0])
  start_min = int((start_time[1].split(" "))[0])
  am_pm = (start_time[1].split(" "))[1]
  time_add = duration.split(":")
  add_hour = int(time_add[0])
  add_min  = int(time_add[1])

  if am_pm == "PM":
    start_hour+=12
  
  result = [start_hour+add_hour , start_min+add_min]
  if result[1]>60:
    result[0]+=1
    result[1]-=60
  n=0
  days =None
  if result[0]>24:
    n = result[0]//24
    result[0] = result[0]%24
    if n == 1:
      days = "(next day)"
    elif n > 1:
      days = "("+str(n)+" days later)"
  
  result_am_pm =''
  if result[0]>12:
    result[0] = result[0]-12 
    result_am_pm = "PM"
  else:
    if result[0] ==12:
      result_am_pm = "PM"
    else:
      if result[0] == 0:
        result[0]=12
      result_am_pm = "AM"
    
  
  hour = str(result[0])
  minu = str(result[1])
  if len(minu)==1:
    minu= "0"+minu

  if day == None:
    new_time =hour+":"+minu+" "+result_am_pm
  elif day !=None:
    result_day = ''
    for d in day_list:
      if d.lower() == day.lower() :
        index = day_list.index(d)
    if index+n >7:
      result_day =day_list[(index+n)%7]
    else:
      result_day = day_list[index+n]
    new_time =hour+":"+minu+" "+result_am_pm+", "+result_day

  if days != None:
    new_time += " "+days

    
    
  return new_time
  
  
  
  
  
  
  
  
  
  import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):

    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

    def test_period_change_at_twelve(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

    def test_twenty_four(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "Friday" to return "12:04 AM, Friday (2 days later)"')

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

if __name__ == "__main__":
    unittest.main()
    
    
    
 # This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)
