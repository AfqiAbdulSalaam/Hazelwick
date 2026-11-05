names = []
for i in range(1,6):
    i = str(i)
    name = input(f"Enter name {i}: ")
    names.append(name)


j = len(names) - 1
while j >= 0:
    print(names[j])
    j = j - 1