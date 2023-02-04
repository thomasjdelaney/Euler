"""For managing anything that we want to do with prime numbers.
Make use of the Sieve of Eratosthenes often."""
import datetime as dt
from typing import List, Optional

import numpy as np


class PrimeNumbersManager:
    """For listing the prime numbers."""

    def __init__(
        self,
        number_of_primes: Optional[int] = None,
        upper_limit: Optional[int] = None,
        lower_limit: Optional[int] = None,
    ) -> None:
        """For initialising the object.
        Args:
            number_of_primes: the number of primes that we want to list.
            upper_limit: list all primes up to this limit
            lower_limit: list all primes above this limit"""
        self.number_of_primes = number_of_primes
        self.upper_limit = upper_limit
        self.lower_limit: int = lower_limit if lower_limit else 0
        self.primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def list_number_of_primes(self) -> List[int]:
        """For making a list of the primes as long a self.number_of_primes"""
        if not self.number_of_primes:
            print(f"{dt.datetime.now()} WARN: Please initialise 'number_of_primes' attribute.")
            return []

        if self.number_of_primes <= len(self.primes_list):
            self.primes_list = self.primes_list[: self.number_of_primes]
        else:
            test = 24
            while len(self.primes_list) < self.number_of_primes:
                test_is_prime = self.is_prime_with_list(test)
                if test_is_prime:
                    self.primes_list.append(test)
                test += 1
        return self.primes_list

    def is_prime_with_list(self, test: int) -> bool:
        """For testing to see if 'test' is a prime number. Uses self.prime_list."""
        is_prime = True
        for p in self.primes_list:
            if 0 == test % p:
                return False
        print(f"{dt.datetime.now()} INFO: {test} is prime.")
        return is_prime

    def list_primes_to_limit(self) -> List[int]:
        """For listing all the prime numbers between self.lower_limit and self.upper_limit."""
        sieved = list(range(2, self.upper_limit + 1))
        iterations = 0
        number_to_test = sieved[iterations]
        while number_to_test < np.sqrt(self.upper_limit):
            sieved = sieved[: iterations + 1] + [s for s in sieved[iterations + 1 :] if s % number_to_test != 0]
            iterations += 1
            number_to_test = sieved[iterations]
            print(f"{dt.datetime.now()} INFO: Sieve has length {len(sieved)}")
        return sieved
