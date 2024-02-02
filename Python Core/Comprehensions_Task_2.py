def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


original_list = [1, 15, 2, 8, 31, 5, 9]
prime_list = [num for num in original_list if is_prime(num)]

print(prime_list)