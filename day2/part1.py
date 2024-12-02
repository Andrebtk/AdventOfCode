f = open("input.txt", "r")


res = 0
for line in f:
    numbers = list(map(int, line.split()))

    safe = True
    inc = False
    
    fst = numbers[0]
    snd = numbers[1]
    diff = snd - fst

    if diff ==0 or abs(diff) > 3:
        safe=False

    inc = fst<snd
    for i in numbers[2:]:
        diff2 = abs(i-snd)

        if diff2 == 0 or abs(diff2) > 3:
            safe=False
            break
        if inc:
            if i < snd:
                safe = False
                break
        else:
            if i > snd:
                safe = False
                break
        snd = i

    if safe:
        res+=1

print(res)