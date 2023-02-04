"""A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, a2+b2=c2

For example, 9+16=25

There exists exactly one Pythagorean triplet for which a+b+c=1000

Find the product abc"""
import numpy as np

pythagorean_sum = lambda x, y: x + y + np.sqrt(np.power(x, 2) + np.power(y, 2))

a = 0
b = 1
difference = 1
solved = False
while pythagorean_sum(a, b) <= 1000 and not solved:
    solved = pythagorean_sum(a, b) == 1000
    if solved:
        break
    a += 1
    b = a + difference
    if pythagorean_sum(a, b) > 1000 and not solved:
        a = 0
        difference += 1
        b = a + difference
    print(f"Trying a={a}, b={b}...")

c = 1000 - a - b
product = a * b * c

print(f"Answer: {product}")
print(f"a = {a}, b = {b}, c = {c}")
