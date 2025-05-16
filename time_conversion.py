# Exercise: Time Conversion
# URL: https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
# Description: Given a time in 12-hour AM/PM format, convert it to military (24-hour) time

def timeConversion(s):
    period = s[-2:]      
    hour = int(s[:2])     
    rest = s[2:-2]       

    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return hour + rest
