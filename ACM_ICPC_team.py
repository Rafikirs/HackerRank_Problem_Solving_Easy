# Exercise: ACM ICPC Team
# URL: https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
# Description: Find the maximum number of topics a 2-person team can know, and how many teams achieve that

def acmTeam(topic):
    max_score = 0
    team_count = 0

    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            combined = bin(int(topics[i], 2) | int(topics[j], 2))
            score = combined.count('1')

            if score > max_score:
                max_score = score
                team_count = 1
            elif score == max_score:
                team_count += 1

    return max_score, team_count
