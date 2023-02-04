"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
from collections.abc import Iterable
from typing import Any, Dict, List, Set

import numpy as np

from py.utils import *


def flatten(xs) -> Any:
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


class PrimeFactors:
    """A class for managing the prime factors of a given integer."""

    def __init__(self, n: Optional[int] = None, d: Optional[Dict[int, int]] = None):
        """For initialising the object either from an int or a dictionary of prime factor -> degree
        Args:
            n: the integer to factorise
            d: the prime_factors -> degree dictionary"""
        self.n: Optional[int] = None
        self.prime_factor_list: Optional[List[n]] = None
        self.degrees: Optional[List[int]] = None
        self.prime_factor_set: Optional[Set] = None
        self.prime_factor_dict: Optional[Dict[int, int]] = None
        if n is not None and d is None:
            self.int_init(n)
        if d is not None and n is None:
            self.dict_init(d)
        self.prime_factor_set = set(self.prime_factor_list)

    def int_init(self, n: int) -> None:
        """For initialising the PrimeFactors object.
        Args:
            n: the number to factorise"""
        self.n = n
        self.prime_factor_list, self.degrees = np.unique(get_prime_factors(self.n), return_counts=True)
        self.prime_factor_dict = {pf: d for pf, d in zip(self.prime_factor_list, self.degrees)}

    def dict_init(self, d: Dict[int, int]):
        """For initialising the Prime Factors object with a dict of prime factors
        Args:
            d: prime factor -> degree"""
        self.prime_factor_dict = d
        self.prime_factor_list = np.array(list(d.keys()))
        self.degrees = list(d.values())
        self.n = 1
        for prime_factor, degree in d.items():
            self.n *= np.power(prime_factor, degree)


list_to_check = range(1, 21)
prime_factor_collection = {}
for n in list_to_check:
    if is_prime(n) and n not in prime_factor_collection:
        prime_factor_collection[n] = 1
    else:
        pfn = PrimeFactors(n=n)
        for pf, d in pfn.prime_factor_dict.items():
            prime_factor_collection[pf] = max(prime_factor_collection[pf], d)

big_pf = PrimeFactors(d=prime_factor_collection)
print(big_pf.n)
