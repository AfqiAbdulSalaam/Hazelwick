readings = [4,7,4,2,9,7,1,2]
uniqueNumbers = []
count = 0

for i in range(len(readings)):
    if i not in uniqueNumbers:
        uniqueNumbers.append(i)
        count = count + 1

duplicateNumbers = len(readings) - count

original = print(readings)
print(f"Without duplicates = {uniqueNumbers}")
print("Duplicates removed: ",duplicateNumbers)