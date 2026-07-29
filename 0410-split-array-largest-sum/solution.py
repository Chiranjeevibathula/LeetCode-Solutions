class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasable(max_sum)->bool:
            current_sum=0
            subarray_count=1
            for num in nums:
                if current_sum+num>max_sum:
                    current_sum=num
                    subarray_count+=1
                else:
                    current_sum+=num
            return subarray_count<=k
        left,right=max(nums),sum(nums)
        first_true_index=-1
        while left<=right:
            mid=(left+right)//2
            if feasable(mid):
                first_true_index=mid
                right=mid-1
            else:
                left=mid+1
        return first_true_index            




        
