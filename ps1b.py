import math
odd_num = 3
prime_num = 2
n = 17327
log_sum = math.log(2)
is_prime = True
while prime_num < n:
    for x in range(2, (odd_num//2)):
        if odd_num % x == 0:
            is_prime = False
    if is_prime:
        prime_num = odd_num
        log_sum = log_sum + math.log(prime_num)
    odd_num = odd_num + 2
    is_prime = True
print("sum:", log_sum, end='\n')
print("ratio:", log_sum/n, end='\n')