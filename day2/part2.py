def safeFunc(numbers):

    inc = numbers[1] > numbers[0]  
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff == 0 or diff > 3: 
            return numbers[i]

        if inc:
            if numbers[i] < numbers[i - 1]: 
                return numbers[i]
        else:
            if numbers[i] > numbers[i - 1]:
                return numbers[i]

    return -1 


def is_safe_after_removal(numbers):
    for i in range(len(numbers)):
        modified_sequence = numbers[:i] + numbers[i + 1:]
        if safeFunc(modified_sequence) == -1:  
            return True
    return False


res = 0
with open("input.txt", "r") as f:
    for line in f:
        numbers = list(map(int, line.split()))
        if safeFunc(numbers) == -1: 
            res += 1
        elif is_safe_after_removal(numbers):  
            res += 1

print("res:", res)
