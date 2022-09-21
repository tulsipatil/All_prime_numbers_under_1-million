n = 1000000
number_range = set(range(2, n+1))
primes_list = []

while number_range:
    prime = number_range.pop()
    primes_list.append(prime)
    multiples = set(range(prime * 2, n+1, prime))
    number_range.difference_update(multiples)
    
#print(primes_list)
prime_count = len(primes_list)
largest_prime = max(primes_list)
print(f"There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")
