rolls = [3,6,1,6,2,5,6,3,1,4]
index = []

num = int(input("Enter a number between 1 and 6: "))
count = 0

for i in range(10):
    if rolls[i] == num:
        index.append(i)
        count = count + 1

print(f"{num} was rolled {count} time(s), at index {index}")