class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome, considering only alphanumeric characters
        and ignoring case differences.

        Args:
            s: Input string to check

        Returns:
            True if the string is a palindrome, False otherwise
        """
        # Initialize two pointers at the start and end of the string
        left_index = 0
        right_index = len(s) - 1

        # Continue checking while the pointers haven't crossed
        while left_index < right_index:
            # Skip non-alphanumeric character on the left
            if not s[left_index].isalnum():
                left_index += 1
            # Skip non-alphanumeric character on the right
            elif not s[right_index].isalnum():
                right_index -= 1
            # Check if characters don't match (case-insensitive)
            elif s[left_index].lower() != s[right_index].lower():
                return False
            # Characters match, move both pointers inward
            else:
                left_index += 1
                right_index -= 1

        # All characters matched successfully
        return True
