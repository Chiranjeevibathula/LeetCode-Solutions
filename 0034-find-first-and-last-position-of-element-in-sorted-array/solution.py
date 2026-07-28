class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        def findFirstTrue(findGreater: bool) -> int:
            left, right = 0, n - 1
            firstTrueIndex = -1

            while left <= right:
                mid = (left + right) // 2
                if findGreater:
                    feasible = nums[mid] > target
                else:
                    feasible = nums[mid] >= target

                if feasible:
                    firstTrueIndex = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return firstTrueIndex

        firstIdx = findFirstTrue(False)
        if firstIdx == -1 or nums[firstIdx] != target:
            return [-1, -1]

        afterLastIdx = findFirstTrue(True)
        if afterLastIdx == -1:
            lastIdx = n - 1
        else:
            lastIdx = afterLastIdx - 1

        return [firstIdx, lastIdx]
