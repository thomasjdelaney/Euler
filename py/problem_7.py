"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""
import datetime as dt
from typing import List


class PrimeNumbersList:
    """For listing the prime numbers."""

    def __init__(self, n: int) -> None:
        """For initialising the object.
        Args:
            n: the number of primes that we want to list."""
        self.n = n
        self.primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def list_primes(self) -> List[int]:
        """For making a list of the primes as long a self.n"""
        if self.n <= len(self.primes_list):
            self.primes_list = self.primes_list[: self.n]
        else:
            test = 24
            while len(self.primes_list) < self.n:
                test_is_prime = self.is_prime_with_list(test)
                if test_is_prime:
                    self.primes_list.append(test)
                test += 1
        return self.primes_list

    def is_prime_with_list(self, test: int) -> bool:
        is_prime = True
        for p in self.primes_list:
            if 0 == test % p:
                return False
        return is_prime


pnl = PrimeNumbersList(10001)
start_all = dt.datetime.now()
primes_list = pnl.list_primes()
end_all = dt.datetime.now()
print(f"Answer: {primes_list[-1]}")
print(f"Time taken: {end_all - start_all}")
