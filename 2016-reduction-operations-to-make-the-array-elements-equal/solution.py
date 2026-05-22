class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total_operations=0
        distinct_count=0
        for prev_num,curr_num in pairwise(nums):
            if prev_num!=curr_num:
                distinct_count+=1
            total_operations+=distinct_count  
        return total_operations    
        
