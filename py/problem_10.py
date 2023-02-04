"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import datetime as dt

from PrimeNumberManager import PrimeNumbersManager

start = dt.datetime.now()
prime_numbers_manager = PrimeNumbersManager(upper_limit=2000000)
primes_to_limit = prime_numbers_manager.list_primes_to_limit()
answer = sum(primes_to_limit)
end = dt.datetime.now()
print(f"{dt.datetime.now()} INFO: The answer is {answer}.")
print(f"{dt.datetime.now()} INFO: Time taken {end - start}.")
