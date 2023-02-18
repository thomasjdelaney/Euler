"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Ashley says: We have to move 2N times to get from one corner to the other.
 We have to enumerate the number of ways of choosing N moves from 2N possible moves. N moves will be to the right, the
 other N moves will be down. So the answer for an NxN grid is 2N choose N.
"""
from math import comb

grid_size = 20
ans = comb(2*grid_size, grid_size)

print(f"Answer: {ans}")
