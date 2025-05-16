# Exercise: Angry Professor
# URL: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
# Description: 
# Determine if a class is canceled based on how many students arrive on time (arrival time ≤ 0). 
# If fewer than k students are on time, return "YES"; otherwise, return "NO"

def angryProfessor(k, a):
    on_time = sum(1 for time in a if time <= 0)
    return "NO" if on_time >= k else "YES"
