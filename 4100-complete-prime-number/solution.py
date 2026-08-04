from math import isqrt


class Solution:
    def completePrime(self, num: int) -> bool:
        # Helper that checks whether a single integer is prime.
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            # Test divisibility only up to the integer square root of value.
            # all(...) returns False as soon as a divisor is found.
            return all(value % divisor for divisor in range(2, isqrt(value) + 1))

        digits = str(num)

        # Check every prefix: build the number digit by digit from the left.
        # e.g. for "239" -> 2, 23, 239
        prefix = 0
        for char in digits:
            prefix = prefix * 10 + int(char)
            if not is_prime(prefix):
                return False

        # Check every suffix: build the number digit by digit from the right.
        # e.g. for "239" -> 9, 39, 239
        suffix, place_value = 0, 1
        for char in reversed(digits):
            suffix = place_value * int(char) + suffix
            place_value *= 10
            if not is_prime(suffix):
                return False

        # All prefixes and suffixes are prime.
        return True

