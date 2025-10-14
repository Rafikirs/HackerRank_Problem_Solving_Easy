# Exercise: Nested Lists
# URL: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Description: Trouver les étudiants ayant la deuxième plus basse note parmi une liste d’étudiants avec leurs scores, et afficher leurs noms par ordre alphabétique

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
        
    records.sort(key=lambda x: x[1])
    scores = sorted({score for student, score in records})
    
    second_lowest = [student for student, score in records if score == scores[1]]
    
    for student in sorted(second_lowest):
        print(student)
