class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluates a mathematical expression string containing +, -, parentheses, and spaces.
        Uses a stack-based approach to handle nested parentheses.
      
        Args:
            s: Input string expression
          
        Returns:
            Integer result of the evaluated expression
        """
        stack = []
        current_result = 0
        current_sign = 1  # 1 for positive, -1 for negative
        index = 0
        length = len(s)
      
        while index < length:
            char = s[index]
          
            # Parse multi-digit numbers
            if char.isdigit():
                number = 0
                digit_start = index
              
                # Continue reading digits to form the complete number
                while digit_start < length and s[digit_start].isdigit():
                    number = number * 10 + int(s[digit_start])
                    digit_start += 1
              
                # Apply the current sign to the number and add to result
                current_result += current_sign * number
              
                # Adjust index to account for multi-digit parsing
                index = digit_start - 1
              
            # Handle addition operator
            elif char == "+":
                current_sign = 1
              
            # Handle subtraction operator
            elif char == "-":
                current_sign = -1
              
            # Handle opening parenthesis
            elif char == "(":
                # Save current state before entering new scope
                stack.append(current_result)
                stack.append(current_sign)
              
                # Reset for new expression inside parentheses
                current_result = 0
                current_sign = 1
              
            # Handle closing parenthesis
            elif char == ")":
                # Pop the sign before the parenthesis
                prev_sign = stack.pop()
                # Pop the result before the parenthesis
                prev_result = stack.pop()
              
                # Apply the sign to current result and combine with previous
                current_result = prev_sign * current_result + prev_result
          
            # Skip spaces implicitly (no action needed)
          
            index += 1
          
        return current_result
