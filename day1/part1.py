f = open("day1Input.txt", "r")

lst1 = []
lst2 = []

for x in f:
    data = x.split()
    lst1.append(int(data[0]))
    lst2.append(int(data[1]))

lst1.sort()
lst2.sort()

res = 0
for i in range(len(lst1)):  
    res += abs(lst1[i] - lst2[i])

print(res)  
f.close()