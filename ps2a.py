n = [0, 0]
result = 0
for a in range(0, 8):
    for b in range(0, 6):
        for c in range(0, 3):
            sum = 6 * a + 9 * b + 20 * c
            if sum < 50 and sum not in n:
                n.append(sum)
            n = sorted(n)
            # print(n)
            # if n[-1] - n[-2] != 1:
            #     result = n[-1] - 1
i = -1
j = -2
while n[i] - n[j] == 1:
    i -= 1
    j -= 1
result = n[i] - 1
print("Largest number of McNuggets that cannot be bought in exact quantity:", result)