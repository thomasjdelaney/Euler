"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
*see files/long_numbers.txt*
"""
import os
from pathlib import Path

from utils import long_summation

long_numbers_file = Path(os.getenv("HOME")) / "Euler" / "files" / "long_numbers.txt"
with open(long_numbers_file) as file:
    str_numbers_list = file.readlines()

numbers_list = []
for str_n in str_numbers_list:
    row_list = [int(n) for n in str_n if n != "\n"]
    numbers_list.append(row_list)


ans = long_summation(numbers_list)
print("".join([str(n) for n in ans]))
