class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree=Counter(dest for src,dest in edges)
        result=[v for v in range(n) if in_degree[v]==0]
        return result
        
