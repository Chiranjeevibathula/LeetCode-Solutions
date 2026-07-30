class Solution:
    def minLength(self, s: str) -> int:
        # Initialize stack with empty string as sentinel to avoid index errors
        stack = [""]
      
        # Process each character in the input string
        for char in s:
            # Check if current character forms "AB" or "CD" pattern with stack top
            if (char == "B" and stack[-1] == "A") or (char == "D" and stack[-1] == "C"):
                # Remove the previous character as it forms a removable pair
                stack.pop()
            else:
                # Add current character to stack if no pattern is formed
                stack.append(char)
      
        # Return final length (subtract 1 for the sentinel empty string)
        return len(stack) - 1
