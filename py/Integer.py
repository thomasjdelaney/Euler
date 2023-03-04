"""
A class for doing more things with an integer
"""
from itertools import combinations
from typing import List, Set, Union

import numpy as np


class Integer:
    def __init__(self, value: int) -> None:
        """For initialising the object.
        Args:
            value: the python integer"""
        self.value = value

    def prime_factors(self) -> List[int]:
        """For getting a list of the prime factors of the Integer"""
        temp_value = self.value
        k = 2
        factors = []
        while k * k <= temp_value:
            while temp_value % k == 0:
                factors.append(k)
                temp_value //= k
            k += 1
        if temp_value > 1:
            factors.append(temp_value)
        return factors

    def divisors(self) -> Set[int]:
        """For getting the divisors of the given integer."""
        divisors = {1}
        prime_factors = self.prime_factors()
        for i in range(len(prime_factors) + 1):
            combo = combinations(prime_factors, i)
            [divisors.add(np.prod(c)) for c in combo]
        return divisors
