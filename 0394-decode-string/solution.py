class Solution:
    def decodeString(self, s: str) -> str:
        # Stack to store repetition counts
        count_stack = []
        # Stack to store intermediate string results
        string_stack = []
        # Current number being parsed (can be multi-digit)
        current_num = 0
        # Current string being built
        current_string = ''
      
        for char in s:
            if char.isdigit():
                # Build multi-digit number (e.g., "30" -> 30)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Opening bracket: push current state to stacks and reset
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ''
            elif char == ']':
                # Closing bracket: pop from stacks and build result
                # Pop the string before this bracket group
                prev_string = string_stack.pop()
                # Pop the repetition count for this bracket group
                repeat_count = count_stack.pop()
                # Combine: previous string + (current string repeated n times)
                current_string = prev_string + current_string * repeat_count
            else:
                # Regular character: append to current string
                current_string += char
      
        return current_string
        
