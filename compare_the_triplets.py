# Exercise: Compare the triplets
# URL: https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
# Description: Given two lists of three scores for Alice and Bob, compare each category: 
# 1 point goes to the person with the higher score; no points for ties. 
# Return their total points as [Alice_score, Bob_score].

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    return [alice_score, bob_score]
