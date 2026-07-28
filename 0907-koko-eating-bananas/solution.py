class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum eating speed to consume all banana piles within h hours.

        Args:
            piles: List of integers representing the number of bananas in each pile
            h: Maximum hours available to eat all bananas

        Returns:
            Minimum integer eating speed (bananas per hour) to finish all piles
        """

        def feasible(eating_speed: int) -> bool:
            """
            Check if all piles can be consumed within h hours at given eating speed.
            Returns True if eating_speed is fast enough to finish in time.
            """
            total_hours = sum((pile_size + eating_speed - 1) // eating_speed
                            for pile_size in piles)
            return total_hours <= h

        # Binary search for the minimum valid eating speed
        # Search space: [1, max(piles)]
        left, right = 1, max(piles)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                # mid is fast enough, record it and try smaller speeds
                first_true_index = mid
                right = mid - 1
            else:
                # mid is too slow, need faster speed
                left = mid + 1

        return first_true_index
