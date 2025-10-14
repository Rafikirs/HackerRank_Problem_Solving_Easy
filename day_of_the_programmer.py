# Exercise: Day of the Programmer
# URL: https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# Description: Finding the 256th day of the year based on certain rules

def dayOfProgrammer(year):
    if year%4 != 0 and year != 1918:
        return f"13.09.{year}"
    elif year%400 == 0:
        return f"12.09.{year}"
    elif year < 1918:
        if year%4 == 0:
            return f"12.09.{year}"
    elif year == 1918:
        return f"26.09.{year}"
    else:
        if year%4 == 0 and year%100 != 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
