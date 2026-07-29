from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
        Find the minimum speed needed to reach the destination within the given time.

        Args:
            dist: List of distances for each train segment
            hour: Maximum time allowed to complete the journey

        Returns:
            Minimum speed required, or -1 if impossible
        """

        def can_reach_in_time(speed: int) -> bool:
            """
            Check if we can complete the journey within the time limit at given speed.

            For all trains except the last, we must wait for the next integer hour.
            For the last train, we can arrive at any fractional time.
            """
            total_time = 0
            n = len(dist)

            for index, distance in enumerate(dist):
                travel_time = distance / speed

                if index == n - 1:
                    total_time += travel_time
                else:
                    total_time += ceil(travel_time)

            return total_time <= hour

        # If we have more trains than available hours (rounded up), it's impossible
        if len(dist) > ceil(hour):
            return -1

        # Binary search using the standard template
        left, right = 1, 10**7
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if can_reach_in_time(mid):  # feasible condition
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index

