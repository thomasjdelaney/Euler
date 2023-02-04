from typing import List, Optional

import numpy as np


def find_first_prime_factor(n: int) -> Optional[int]:
    """For finding the first prime factor of the given integer.
    Args:
        n: int
    Returns:
        first_prime_factor: The first prime factor of the give number."""
    for i in range(2, int(np.sqrt(n)) + 1):
        if (n % i) == 0:
            return i
    return None


def is_prime(n: int) -> bool:
    """For finding out if a number is prime or not.
    Args:
        n: integer
    Returns:
        bool"""
    if n == 1:
        return False
    else:
        return find_first_prime_factor(n) is None


def get_prime_factors(n: int) -> List[int]:
    """For finding the prime factors of n.
    Args:
        n: integer to factor
    Returns:
        a list of prime factors of n"""
    if is_prime(n) or n == 1:  # n is prime or 1
        return []

    prime_factors = []
    to_factor = n
    while not is_prime(to_factor):
        first_factor = find_first_prime_factor(to_factor)
        prime_factors.append(first_factor)
        to_factor = to_factor // first_factor
    prime_factors.append(to_factor)
    return prime_factors


def is_palindromic(n: int) -> bool:
    """checks if n in a palindromic number"""
    str_n = str(n)
    return str_n == str_n[::-1]
