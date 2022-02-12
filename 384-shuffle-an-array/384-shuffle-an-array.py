class Solution:

    def __init__(self, nums: List[int]):
        self.sol = nums

    def reset(self) -> List[int]:
        return self.sol

    def shuffle(self) -> List[int]:
        temp = self.sol[:]
        for i in range(len(temp)):
            j = randint(i, len(temp)-1)
            temp[i], temp[j] = temp[j], temp[i]
        return temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()