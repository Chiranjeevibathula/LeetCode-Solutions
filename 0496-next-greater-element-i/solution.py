class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater_element={}
        for num in nums2[::-1]:
            while stack and stack[-1]<num:
                stack.pop()
            if stack:
                next_greater_element[num]=stack[-1]
            stack.append(num)
        return [next_greater_element.get(num,-1) for num in nums1]         



              

        
