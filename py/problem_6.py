"""The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
sum."""
from itertools import combinations

import numpy as np

list_to_check = range(1, 101)

combos = combinations(list_to_check, 2)
ans = 2 * sum([np.prod(c) for c in combos])
print(ans)
