class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
      
        # Iterate through all possible palindrome centers
        # For a string of length n, there are (2n - 1) possible centers:
        # n centers at each character (for odd-length palindromes)
        # n-1 centers between characters (for even-length palindromes)
        for center in range(2 * n - 1):
            # Calculate left and right pointers based on center position
            # For even center values (0, 2, 4...): left = right = center // 2
            # For odd center values (1, 3, 5...): left = center // 2, right = center // 2 + 1
            left = center // 2
            right = (center + 1) // 2
          
            # Expand around center while characters match
            while left >= 0 and right < n and s[left] == s[right]:
                # Found a palindrome
                count += 1
                # Expand outward
                left -= 1
                right += 1
              
        return count
        
