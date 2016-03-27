###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6, 9, 20)   # variable that contains package sizes

numCanBuy = []
for a in range(0, 200//packages[0]+1):
    for b in range(0, 200//packages[1]+1):
        for c in range(0, 200//packages[2]+1):
            sum = packages[0] * a + packages[1] * b + packages[2] * c
            if sum <= 200 and sum not in numCanBuy:
                numCanBuy.append(sum)
            numCanBuy = sorted(numCanBuy)

for n in range(1, 200):   # only search for solutions up to size 200
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    if n not in numCanBuy:
        bestSoFar = n
print("Given package sizes ", packages[0],", ", packages[1], ", and ", packages[2],", the largest number of McNuggets that cannot be bought in exact quantity is: ", bestSoFar, sep='', end='\n')