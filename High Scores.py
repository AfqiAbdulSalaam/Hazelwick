name = " "
names = []
scores = []
highescore = 0
highestname = " "
total = 0
aboveAverage = " "

while name != "done":
    if name != "done":
        playername = input("Player name (or 'done')")
        names.append(playername)
        playerscore = int(input("Score for ",playername,": "))
        scores.apppend(playerscore)
    elif name == "done":
        break

average = total/len(scores)

for i in range(len(scores)):
    total = total + scores[i]
    if scores[i] > highscore:
        highscore = scores[i]
        index = scores[i]
        highestname = names(index)

average = total/len(scores)

for i in range(len(scores)):
    if scores[i] > average:
    aboveAverage = names[i]

print("Top Scorer = ",highestname)
print("Average Score = ",average)
print("Above Average = ",aboveAverage)


