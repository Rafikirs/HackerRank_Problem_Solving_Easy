# Exercise: Grading Students
# URL: https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
# Description: Given a list of student grades, round each up to the next multiple of 5 
# only if the grade is ≥38 and the difference to the next multiple is less than 3.
# Return the list of final grades after applying this rule

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            if next_multiple_of_5 - grade < 3:
                result.append(next_multiple_of_5)
            else:
                result.append(grade)
    return result
