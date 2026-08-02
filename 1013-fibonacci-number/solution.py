class Solution:
    def fib(self, n: int) -> int:
        current, next_fib = 0, 1
        for _ in range(n):
            current, next_fib = next_fib, current + next_fib
        return current
