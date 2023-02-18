"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from typing import List


def collatz_iteration(n: int) -> int:
    """For applying an iteration of the hailstone sequence. https://en.wikipedia.org/wiki/Collatz_conjecture
    Args:
        n: the integer
    Return:
        the result after applying the sequence for one iteration."""
    return n // 2 if n % 2 == 0 else (3 * n) + 1


class HailstoneSequence:
    """A class for defining a hailstone sequence starting from the given integer."""
    def __init__(self, start: int) -> None:
        """For initialising the object.
        Args:
            start: the starting integer for the sequence"""
        if start <= 0:
            raise ValueError(f"Stating point must be a natural number! {start}")

        self.start = start
        self.sequence: List[int] = [start]
        self.set_sequence()

    def set_sequence(self):
        s = self.start
        while s != 1:
            s = collatz_iteration(s)
            self.sequence.append(s)


class HailstoneSequenceLengths:
    """A class for getting the lengths of all the hailstone sequences for all the numbers in the given list"""
    def __init__(self, number_list: List[int]):
        self.number_list = number_list
        self.number_list.sort(reverse=True)
        self.sequence_lengths = {}
        self.set_sequence_lengths()

    def set_sequence_lengths(self):
        for n in self.number_list:
            if n not in self.sequence_lengths:
                hail_stone_seq = HailstoneSequence(n)
                for i, sn in enumerate(hail_stone_seq.sequence):
                    self.sequence_lengths[sn] = len(hail_stone_seq.sequence) - i


hsl = HailstoneSequenceLengths(list(range(1, 1000000)))
answer = max(hsl.sequence_lengths, key=hsl.sequence_lengths.get)
print(f"Answer: {answer}")
