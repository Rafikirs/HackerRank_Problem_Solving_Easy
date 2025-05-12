def timeConversion(s):
    period = s[-2:]       # AM ou PM
    hour = int(s[:2])     # Heure en entier
    rest = s[2:-2]        # Minutes et secondes : ":MM:SS"

    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return hour + rest
