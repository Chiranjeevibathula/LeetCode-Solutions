from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Find the maximum minimum distance between m balls placed in given positions.
        Uses binary search template to find the first distance where placement fails.
        """

        def can_place_balls(min_distance: int) -> bool:
            """
            Check if we can place m balls with at least min_distance apart.
            Returns True if placement is possible, False otherwise.
            """
            balls_placed = 1  # Place first ball at position[0]
            previous_position = position[0]

            for i in range(1, len(position)):
                if position[i] - previous_position >= min_distance:
                    balls_placed += 1
                    previous_position = position[i]
                    if balls_placed == m:
                        return True

            return False

        # Sort positions to enable greedy placement
        position.sort()

        # Binary search using the standard template
        # Feasible function: NOT can_place_balls(d) - true when we cannot place m balls
        left, right = 1, position[-1] - position[0]
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if not can_place_balls(mid):
                # Feasible: cannot place m balls with this distance
                first_true_index = mid
                right = mid - 1
            else:
                # Not feasible: can still place m balls, try larger distance
                left = mid + 1

        # The answer is the largest distance where we CAN place all balls
        if first_true_index == -1:
            # All distances work, return the maximum
            return position[-1] - position[0]
        else:
            # Return the distance just before placement becomes impossible
            return first_true_index - 1

