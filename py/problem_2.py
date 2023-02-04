from typing import List


def fibonacci_to_limit(limit: int) -> List[int]:
    prev = 0
    current = 1
    fibonacci_numbers = [prev, current]
    while current + prev < limit:
        next_fib = prev + current
        prev = current
        current = next_fib
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers


fibs_to_limit: List[int] = fibonacci_to_limit(4000000)
ans = sum(f for f in fibs_to_limit if (f > 0) & (f % 2 == 0))
print(ans)
