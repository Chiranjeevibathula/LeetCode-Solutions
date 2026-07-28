class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Find the minimum ship capacity needed to ship all packages within given days.

        Args:
            weights: List of package weights
            days: Maximum number of days to ship all packages

        Returns:
            Minimum ship capacity required
        """

        def feasible(capacity):
            """
            Check if all packages can be shipped within the given days
            using a ship with the specified capacity.
            Returns True if capacity is sufficient (feasible), False otherwise.
            """
            current_weight = 0
            days_needed = 1

            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    days_needed += 1
                    current_weight = weight

            return days_needed <= days

        # Binary search bounds
        left = max(weights)  # Minimum: must carry heaviest package
        right = sum(weights)  # Maximum: ship everything in one day
        first_true_index = -1

        # Binary search template: find first capacity where feasible(capacity) is True
        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1  # Search for smaller valid capacity
            else:
                left = mid + 1

        return first_true_index
