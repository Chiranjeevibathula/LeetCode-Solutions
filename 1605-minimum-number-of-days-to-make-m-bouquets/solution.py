class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Find the minimum number of days to wait to make m bouquets from the garden.
        Each bouquet requires k adjacent flowers to bloom.

        Args:
            bloomDay: List where bloomDay[i] is the day when the i-th flower blooms
            m: Number of bouquets needed
            k: Number of adjacent flowers needed for each bouquet

        Returns:
            Minimum number of days to wait, or -1 if impossible
        """

        # Early termination: impossible if we don't have enough flowers
        if m * k > len(bloomDay):
            return -1

        def feasible(days: int) -> bool:
            """
            Check if we can make m bouquets after waiting 'days' days.
            Returns True if we can make at least m bouquets.
            """
            bouquets_made = 0
            consecutive_bloomed = 0

            for bloom_day in bloomDay:
                if bloom_day <= days:
                    consecutive_bloomed += 1
                    if consecutive_bloomed == k:
                        bouquets_made += 1
                        consecutive_bloomed = 0
                else:
                    consecutive_bloomed = 0

            return bouquets_made >= m

        # Binary search using the template pattern
        left, right = min(bloomDay), max(bloomDay)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if feasible(mid):
                first_true_index = mid
                right = mid - 1  # Search for earlier day
            else:
                left = mid + 1

        return first_true_index
