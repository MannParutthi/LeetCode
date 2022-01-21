class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteDict = {x:[] for x in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisiteDict[course].append(prerequisite)
        result = []
        visited = []
        cycle = []
        
        def dfs(course):
            if course in cycle: return False # False means cycle detected and can not proceed ahead
            if course in visited: return True
            
            cycle.append(course)
            for prerequisite in prerequisiteDict[course]:
                if dfs(prerequisite) == False: return False
            cycle.remove(course)
            
            visited.append(course)
            result.append(course)
        
        for c in range(numCourses):
            if dfs(c) == False: 
                return False
        return True