# Exercise: Breaking the records
# URL: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
# Description: 
# Maria tracks how many times she breaks her season records for highest and lowest game scores. 
# The first game's score sets both records, and she counts how often she beats them throughout the season.
# The result is a list: [most_record_breaks, least_record_breaks].

def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1

    return max_count, min_count
