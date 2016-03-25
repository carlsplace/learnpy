i = 1
odd_num = 3
prime_num = 0
is_prime = True
while i < 1992:
    for x in range(2, (odd_num//2)):
        if odd_num % x == 0:
            is_prime = False
    if is_prime:
        prime_num = odd_num
        i = i + 1
    odd_num = odd_num + 2
    is_prime = True
print(prime_num, end='\n')