# Print out every prime number between 1 and 1000.

for i in range(2, 1000+1):
    is_prime = True
    for div in range(2, i//2+1):
        if i % div == 0:
            is_prime = False

    if is_prime:
        print(i)
