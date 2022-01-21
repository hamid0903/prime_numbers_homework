from is_prime import is_prime
#Define function, Find the all prime numbers which are less than n.
def prime_list(n:int)->list:
    """
    Find the all prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        list: List of prime numbers
    """
    prime_list = []
    for i in range(1, n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

print(prime_list(100))