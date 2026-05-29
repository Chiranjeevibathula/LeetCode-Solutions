class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start:int,current_combination:List[int])->None:
            if len(current_combination)==k:
                result.append(current_combination[:])
                return
            if start>n:
                return 
            current_combination.append(start)
            backtrack(start+1,current_combination)
            current_combination.pop()
            backtrack(start+1,current_combination)
        result:List[List[int]]=[]
        temp_combination:List[int]=[]
        backtrack(1,temp_combination)
        return result    

        
