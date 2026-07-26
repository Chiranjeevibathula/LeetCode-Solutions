class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n-1):
            complement=target-numbers[i]
            left,right=i+1,n-1
            first_true_index=-1
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]>=complement:
                    first_true_index=mid
                    right=mid-1
                else:
                    left=mid+1
            if first_true_index!=-1 and numbers[first_true_index]==complement:
                return [i+1,first_true_index+1]    
        return []               




