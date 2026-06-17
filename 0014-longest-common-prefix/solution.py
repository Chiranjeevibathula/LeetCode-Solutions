class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Iterate through each character position of the first string
        for i in range(len(strs[0])):
            # Check this position against all other strings in the array
            for string in strs[1:]:
                # If current string is shorter than position i, or
                # character at position i doesn't match the first string's character
                if len(string) <= i or string[i] != strs[0][i]:
                    # Return the common prefix up to (but not including) position i
                    return strs[0][:i]

        # If we've checked all positions without mismatch,
        # the entire first string is the common prefix
        return strs[0]
