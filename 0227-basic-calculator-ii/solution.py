class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluates a mathematical expression string containing +, -, *, / operators.
        Follows standard operator precedence (multiplication and division before addition and subtraction).
      
        Args:
            s: String expression to evaluate
          
        Returns:
            Integer result of the expression
        """
        current_number = 0
        string_length = len(s)
        previous_operator = '+'  # Initialize with '+' to handle the first number
        stack = []
      
        for index, char in enumerate(s):
            # Build multi-digit numbers
            if char.isdigit():
                current_number = current_number * 10 + int(char)
          
            # Process the number when we hit an operator or reach the end of string
            # Skip spaces by checking if char is an operator
            if index == string_length - 1 or char in '+-*/':
                # Apply the previous operator to the current number
                if previous_operator == '+':
                    # Push positive number to stack
                    stack.append(current_number)
                elif previous_operator == '-':
                    # Push negative number to stack
                    stack.append(-current_number)
                elif previous_operator == '*':
                    # Multiply with the last number in stack
                    stack.append(stack.pop() * current_number)
                elif previous_operator == '/':
                    # Divide the last number in stack (truncate towards zero)
                    stack.append(int(stack.pop() / current_number))
              
                # Update operator for next iteration
                previous_operator = char
                # Reset current number for next parsing
                current_number = 0
      
        # Sum all numbers in the stack to get the final result
        return sum(stack)
