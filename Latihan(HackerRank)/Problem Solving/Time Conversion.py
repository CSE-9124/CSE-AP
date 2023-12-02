# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty: Easy

# ======================== Solution ========================
# CARA 1 :
def timeConversion(s):
    hour, minutes, second = s.split(":")

    if "PM" in s:
        hour = int(hour) + 12
        if hour == 24:
            hour = 12
    else:
        hour = int(hour)
        if hour == 12:
            hour = 0

    second = second.replace("AM", "").replace("PM", "")

    return f"{hour:02}:{minutes}:{second}"

s = input()
print(timeConversion(s))


# CARA 2 :
def time_Conversion(s):
    h, m, ss = s.split(':')
    if ss[-2:] == 'AM':
        if h =='12':
            h ='00'
            return h + ':' + m + ':' + ss[:2]
        else:
            ss = ss[:2]
            return h + ':' + m + ':' + ss[:2]
        
    elif ss[-2:] == 'PM':
        if h == '12':
            return h + ':' + m + ':' + ss[:2]
            
        else:
            h = str(int(h)+12)
            return  h + ':' + m + ':' + ss[:2]
        

# ======================== Test Case ========================
s = "12:01:00AM"
print(timeConversion(s))

s = "12:01:00PM"
print(time_Conversion(s))