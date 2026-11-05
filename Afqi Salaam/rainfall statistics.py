rainfall = [12, 0, 7, 25, 3, 18, 0]
DAYS = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
min = 0
max = 0
total = 0
for i in range(len(rainfall)):
    if rainfall[i] < min:
        min = rainfall[i]
    elif rainfall[i] > min:
        max = rainfall[i]
    total = total + rainfall[i]

average = total/len(rainfall)
wettest = 