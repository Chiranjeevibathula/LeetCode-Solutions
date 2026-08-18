class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def is_palindrome(s:str)->bool:
            return s==s[::-1]
        def dfs(s:str,j:int,path:List,ans:List[List[str]])->None:
            if j==len(s):
                ans.append(path)
                return
            for i in range(j,len(s)):
                if is_palindrome(s[j:i+1]):
                    dfs(s,i+1,path+[s[j:i+1]],ans)
        dfs(s,0,[],ans)
        return ans


        