class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def three_way_quick_sort(left:int,right:int)->None:
            if left>right:
                return
            pivot=nums[randint(left,right)]    
            i=left-1
            j=right+1
            k=left
            while k<j:
                if nums[k]<pivot:
                    i+=1
                    nums[i],nums[k]=nums[k],nums[i]
                    k+=1
                elif nums[k]>pivot:
                    j-=1
                    nums[j],nums[k]=nums[k],nums[j]
                else:
                    k+=1
            three_way_quick_sort(left,i)
            three_way_quick_sort(j,right) 
        three_way_quick_sort(0,len(nums)-1)    
        return nums              



        
