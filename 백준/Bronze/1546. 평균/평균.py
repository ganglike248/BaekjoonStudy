N = int(input())
score = list(map(int, input().split()))
newScore = []
maxScore = max(score)

for i in score:
    newScore.append(i / maxScore * 100)

print(sum(newScore) / N)