class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(l:int,r:int,s:str)->None:
            if l>n or r>n or l<r:
                return 
            if l==n and r==n:
                result.append(s)
                return 
            backtrack(l+1,r,s+'(')
            backtrack(l,r+1,s+')')  
        result=[]
        backtrack(0,0,'')
        return result      

        