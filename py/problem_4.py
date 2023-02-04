from itertools import combinations
from typing import List, Tuple

import numpy as np

from py.utils import *


def get_largest_palindromic_number_below_limit(limit: int) -> int:
    """For getting the largest palindromic number below the given limit.
    Args:
        limit: int
    Returns:
        palindromic_number"""
    str_limit = str(limit)
    num_digits = len(str_limit)
    half_num_digits = num_digits // 2
    str_prefix = str_limit[:half_num_digits]
    prefix_reversed_str = str_prefix[::-1]
    prefix_reversed_int = int(prefix_reversed_str)
    suffix_int = int(str_limit[-half_num_digits:])
    is_suffix_lt_reversed_prefix = suffix_int <= prefix_reversed_int
    if num_digits % 2 == 1:  # odd number of digits
        if is_suffix_lt_reversed_prefix:
            palindromic_number = int(str_prefix + str(int(str_limit[half_num_digits]) - 1) + prefix_reversed_str)
        else:
            palindromic_number = int(str_prefix + str(int(str_limit[half_num_digits])) + prefix_reversed_str)
    else:
        if is_suffix_lt_reversed_prefix:
            str_prefix = str(int(str_prefix) - 1)
            palindromic_number = int(str_prefix + str_prefix[::-1])
        else:
            palindromic_number = int(str_prefix + str_prefix[::-1])
    return palindromic_number


def try_make_n_digit_product_from_factors(factors: List[int], n: int) -> Tuple[int, Tuple[int, int]]:
    """Try to make an n digit int from a combination of the largest factor in factors and next largest possible.
    Return 0 if this is not possible.
    Args:
        factors: a list of ints
        n: the number of digits allowed
    Returns:
        either the factor itself or 0"""
    max_product = 0
    max_product_pair = (0, 0)
    for pair in combinations(factors, 2):
        product = np.prod(pair)
        if product > max_product and len(str(product)) <= n:
            max_product = product
            max_product_pair = pair
    return max_product, max_product_pair


def is_product_of_m_n_digit_int(to_check: int, m: int, n: int) -> bool:
    """For checking if the given integer is a product of m integers of n digits
    Args:
        to_check: the int to check
        m: the number of products
        n: the number of digits allowed in the products
    Return:
        bool"""
    is_product = False
    prime_factors = get_prime_factors(to_check)
    has_long_factors = any(map(lambda x: len(str(x)) > n, prime_factors))
    if has_long_factors:
        return False
    factors = prime_factors
    largest_n_digit_product = None
    max_product = None
    while max_product != 0:
        largest_n_digit_product = max_product
        max_product, used_pair = try_make_n_digit_product_from_factors(factors, n)
        if max_product == 0:
            continue
        [factors.remove(u) for u in used_pair]
        factors.append(max_product)
    if len(factors) == m:
        is_product = True
    return is_product


def get_largest_palindromic_number_with_three_digit_prime_factor(starting_limit: int) -> int:
    """Counts down from limit testing each palindromic number
    Args:
        starting_limit: int
    Returns:
        res"""
    is_product_of_three_digit_pair = False
    limit = starting_limit
    while is_product_of_three_digit_pair:
        palindromic_number = get_largest_palindromic_number_below_limit(limit)
        is_product_of_three_digit_pair = is_product_of_m_n_digit_int(to_check=palindromic_number, m=2, n=3)
        limit = palindromic_number
    return limit


three_digit_palindrome_limit = 999 * 999
ans = get_largest_palindromic_number_with_three_digit_prime_factor(starting_limit=three_digit_palindrome_limit)
