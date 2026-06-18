class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import cache
        len_s1,len_s2=len(s1),len(s2)
        if len_s1+len_s2!=len(s3):
            return False
        @cache
        def dfs(index_s1:int,index_s2:int)->bool:
            if index_s1>=len_s1 and index_s2>=len_s2:
                return True
            index_s3=index_s1+index_s2
            if index_s1<len_s1 and s1[index_s1]==s3[index_s3]:
                if dfs(index_s1+1,index_s2):
                    return True
            if index_s2<len_s2 and s2[index_s2]==s3[index_s3]:
                if dfs(index_s1,index_s2+1):
                    return True   
            return False
        return dfs(0,0)                 
                            
        
