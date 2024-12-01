f = open("day1Input.txt", "r")
lst1 = []
lst2 = []

for x in f:
    data = x.split()
    lst1.append(int(data[0]))
    lst2.append(int(data[1]))

similarityScore=0
for i in range(len(lst1)):
    mult=0
    for elem in lst2:
        if lst1[i] == elem:
            mult+=1

    similarityScore += lst1[i] * mult

print(similarityScore)
f.close()