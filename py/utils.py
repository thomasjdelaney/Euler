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
    """For finding the prime factors of number_of_primes.
    Args:
        n: integer to factor
    Returns:
        a list of prime factors of number_of_primes"""
    if is_prime(n) or n == 1:  # number_of_primes is prime or 1
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
    """checks if number_of_primes in a palindromic number"""
    str_n = str(n)
    return str_n == str_n[::-1]


def long_summation(numbers: np.ndarray | List[List[int]]) -> List[int]:
    """A function for automatically doing long summation. stores the results as a list of ints that can be strung
    together to give the answer.
    Args:
        numbers: the list of integers to sum
    Returns:
        list of integers"""
    if isinstance(numbers, list):
        numbers = np.array(numbers)

    long_sum = []
    left_over = 0
    num_rows, num_cols = numbers.shape
    for i, column in enumerate(numbers.T[::-1]):
        col_sum = column.sum() + left_over
        left_over = np.floor_divide(col_sum, 10)
        if i < num_cols - 1:
            long_sum.append(col_sum - 10 * left_over)
        else:
            long_sum.append(col_sum)
    return long_sum[::-1]
