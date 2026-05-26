class Solution:
    def shortestPalindrome(self, s: str) -> str:
         # Rolling hash parameters
        BASE = 131  # Prime base for polynomial rolling hash
        MOD = 10**9 + 7  # Large prime modulus to prevent overflow
      
        n = len(s)
      
        # Hash values for prefix and suffix
        prefix_hash = 0  # Hash of s[0:i+1]
        suffix_hash = 0  # Hash of reverse of s[0:i+1]
      
        # Multiplier for suffix hash calculation
        base_power = 1
      
        # Track the longest palindrome prefix ending position
        longest_palindrome_end = 0
      
        # Iterate through each character to find longest palindrome prefix
        for i, char in enumerate(s):
            # Calculate character value (1-indexed)
            char_value = ord(char) - ord('a') + 1
          
            # Update prefix hash: hash = hash * base + char_value
            prefix_hash = (prefix_hash * BASE + char_value) % MOD
          
            # Update suffix hash: builds hash of reversed string
            # For reversed string, we add new character at the beginning
            suffix_hash = (suffix_hash + char_value * base_power) % MOD
          
            # Update base power for next iteration
            base_power = (base_power * BASE) % MOD
          
            # If hashes match, substring s[0:i+1] is a palindrome
            if prefix_hash == suffix_hash:
                longest_palindrome_end = i + 1
      
        # If entire string is palindrome, return as is
        if longest_palindrome_end == n:
            return s
      
        # Otherwise, prepend the reverse of non-palindrome suffix
        # s[longest_palindrome_end:] is the part that's not palindrome
        non_palindrome_suffix = s[longest_palindrome_end:]
        return non_palindrome_suffix[::-1] + s
        
