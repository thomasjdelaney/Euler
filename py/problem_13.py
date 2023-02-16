"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
*see files/long_numbers.txt*
"""
import os
import numpy as np
from typing import List
from pathlib import Path


long_numbers_file = Path(os.getenv('HOME')) / 'Euler' / 'files' / 'long_numbers.txt'
with open(long_numbers_file) as file:
    str_numbers_list = file.readlines()

numbers_list = []
for str_n in str_numbers_list:
    row_list = [int(n) for n in str_n if n != '\n']
    numbers_list.append(row_list)


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
            long_sum.append(col_sum - 10*left_over)
        else:
            long_sum.append(col_sum)
    return long_sum[::-1]


ans = long_summation(numbers_list)
print(''.join([str(n) for n in ans]))
