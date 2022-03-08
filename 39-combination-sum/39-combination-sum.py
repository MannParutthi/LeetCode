class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(index, currComb, total):
            if total == target:
                res.append(currComb.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            currComb.append(candidates[index]) # curr ele => candidates[index]
            dfs(index, currComb, total + candidates[index]) # 1st way => take curr ele again
            currComb.pop()
            dfs(index+1, currComb, total) # 2nd way => never take curr ele again 
            
        
        dfs(0, [], 0)
        return res