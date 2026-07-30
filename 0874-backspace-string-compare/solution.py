class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compare two strings after processing backspace characters ('#').
        Uses two pointers traversing from the end of each string.
        Time: O(n + m), Space: O(1) where n and m are lengths of s and t.
        """
        # Initialize pointers at the end of both strings
        i = len(s) - 1
        j = len(t) - 1
        skip_s = 0  # Count of backspaces to skip in string s
        skip_t = 0  # Count of backspaces to skip in string t
      
        # Process both strings from right to left
        while i >= 0 or j >= 0:
            # Find the next valid character in string s (after processing backspaces)
            while i >= 0:
                if s[i] == '#':
                    # Found a backspace, increment skip counter
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    # Skip this character due to backspace
                    skip_s -= 1
                    i -= 1
                else:
                    # Found a valid character that won't be deleted
                    break
          
            # Find the next valid character in string t (after processing backspaces)
            while j >= 0:
                if t[j] == '#':
                    # Found a backspace, increment skip counter
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    # Skip this character due to backspace
                    skip_t -= 1
                    j -= 1
                else:
                    # Found a valid character that won't be deleted
                    break
          
            # Compare the current valid characters
            if i >= 0 and j >= 0:
                # Both strings have valid characters to compare
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # One string has a character while the other doesn't
                return False
          
            # Move to the next characters
            i -= 1
            j -= 1
      
        # All characters matched successfully
        return True
