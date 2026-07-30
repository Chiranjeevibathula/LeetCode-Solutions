class Solution:
    def makeGood(self, s: str) -> str:
        """
        Remove adjacent characters that are the same letter but different cases.
      
        Args:
            s: Input string to process
          
        Returns:
            String after removing all bad pairs
        """
        # Use a stack to track characters
        stack = []
      
        for char in s:
            # Check if stack is empty or current char doesn't form a bad pair with top of stack
            # ASCII difference between uppercase and lowercase of same letter is 32
            # e.g., ord('a') - ord('A') = 97 - 65 = 32
            if not stack or abs(ord(stack[-1]) - ord(char)) != 32:
                # Add character to stack if it doesn't form a bad pair
                stack.append(char)
            else:
                # Remove the top character as it forms a bad pair with current character
                stack.pop()
      
        # Join all remaining characters in the stack to form the final string
        return "".join(stack)
        
