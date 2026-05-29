class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        queue=deque([[0]])
        result=[]
        while queue:
            current_path=queue.popleft()
            last_node=current_path[-1]
            if last_node==n-1:
                result.append(current_path)
                continue
            for neighbor in graph[last_node]:
                new_path=current_path+[neighbor]
                queue.append(new_path)
        return result            
        
