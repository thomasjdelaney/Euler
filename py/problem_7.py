"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""
import datetime as dt

from PrimeNumberManager import PrimeNumbersManager

pnm = PrimeNumbersManager(number_of_primes=10001)
start_all = dt.datetime.now()
primes_list = pnm.list_number_of_primes()
end_all = dt.datetime.now()
print(f"Answer: {primes_list[-1]}")
print(f"Time taken: {end_all - start_all}")
