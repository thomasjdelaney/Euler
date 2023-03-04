"""
By starting at the top of the number_triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the number_triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a number_triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""
from typing import List, Tuple


class NumberTriangle:
    """A class for everything related to number triangles, like those in Project Euler questions 18 and 67."""

    def __init__(self, triangle: List[List[int]]) -> None:
        """For initialising the object.
        Args:
            triangle: list of lists, the index of the parent list equals the length of the child-1.
                so len(number_triangle[0])=1, and len(number_triangle[n]) = n+1"""
        self.triangle = triangle

    def get_left_path_value(self) -> int:
        return sum([level[0] for level in self.triangle])

    def get_right_path_value(self) -> int:
        return sum([level[-1] for level in self.triangle])

    def choose(self) -> Tuple[int, "NumberTriangle"]:
        """For excluding the lower value path, and choosing the other way.
        Returns:
            int: the top of the current number_triangle
            NumberTriangle: the NumberTriangle remaining after we make our choice"""
        left_path_value = self.get_left_path_value()
        right_path_value = self.get_right_path_value()
        if left_path_value > right_path_value:
            new_triangle = NumberTriangle([level[:-1] for level in self.triangle[1:]])
        else:
            new_triangle = NumberTriangle([level[1:] for level in self.triangle[1:]])
        return self.triangle[0][0], new_triangle

    def __repr__(self) -> str:
        return "\n".join([str(level) for level in self.triangle])


path = []
number_triangle = NumberTriangle(
    [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
)
while len(number_triangle.triangle) > 0:
    n, number_triangle = number_triangle.choose()
    path.append(n)
print(f"Answer: {sum(path)}")
