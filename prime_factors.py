def get_prime_numbers(n):
    factor = list()
    divisor = 2
    while(divisor <= n):
        if n % divisor == 0:
            factor.append(divisor)
            n = n//divisor
        else:
            divisor += 1
    return factor

get_prime_numbers(300)