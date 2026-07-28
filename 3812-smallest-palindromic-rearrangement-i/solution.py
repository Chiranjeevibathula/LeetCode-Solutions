from collections import Counter
from string import ascii_lowercase


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Count the frequency of each character in the input string
        char_count = Counter(s)

        # Holds the left half of the resulting palindrome
        left_half_parts = []
        # Holds the single middle character (if any character has an odd count)
        middle_char = ""

        # Iterate through characters in alphabetical order to ensure the
        # smallest lexicographical palindrome
        for char in ascii_lowercase:
            # Number of pairs that can be placed symmetrically on both sides
            pair_count = char_count[char] // 2
            left_half_parts.append(char * pair_count)

            # Remove the characters already used in pairs
            char_count[char] -= pair_count * 2

            # If one character remains, it can be used as the middle character
            if char_count[char] == 1:
                middle_char = char

        # Build the left half of the palindrome
        left_half = "".join(left_half_parts)

        # Combine left half, middle character, and the reversed left half
        result = left_half + middle_char + left_half[::-1]

        return result
