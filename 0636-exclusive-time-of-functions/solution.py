class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Calculate exclusive time of each function based on start/end logs.
      
        Args:
            n: Number of functions
            logs: List of log entries in format "function_id:start/end:timestamp"
      
        Returns:
            List of exclusive execution times for each function
        """
        # Stack to track currently running functions
        function_stack = []
      
        # Initialize result array with exclusive times for each function
        exclusive_times = [0] * n
      
        # Track the previous timestamp for calculating time intervals
        previous_timestamp = 0
      
        # Process each log entry
        for log_entry in logs:
            # Parse log entry: function_id:operation:timestamp
            function_id, operation, timestamp = log_entry.split(":")
            function_id = int(function_id)
            current_timestamp = int(timestamp)
          
            # Check if this is a start operation
            if operation == "start":
                # If there's a function currently running, update its exclusive time
                if function_stack:
                    top_function = function_stack[-1]
                    exclusive_times[top_function] += current_timestamp - previous_timestamp
              
                # Push new function onto stack
                function_stack.append(function_id)
                previous_timestamp = current_timestamp
              
            else:  # operation == "end"
                # Pop the ending function and update its exclusive time
                # Add 1 because end timestamp is inclusive
                ending_function = function_stack.pop()
                exclusive_times[ending_function] += current_timestamp - previous_timestamp + 1
              
                # Move to next timestamp after the end
                previous_timestamp = current_timestamp + 1
      
        return exclusive_times
        
