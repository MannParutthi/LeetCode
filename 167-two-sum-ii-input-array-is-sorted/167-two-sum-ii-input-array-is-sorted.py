class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtrIndex = 0
        rightPtrIndex = len(numbers) - 1
        
        while leftPtrIndex < rightPtrIndex:
            if numbers[leftPtrIndex] + numbers[rightPtrIndex] > target:   
                rightPtrIndex -= 1 # decrement right ptr as arr is sorted and sum > target so we need to decrease the sum
            elif numbers[leftPtrIndex] + numbers[rightPtrIndex] < target:
                leftPtrIndex += 1 # increment left ptr as arr is sorted and sum < target so we need to increase the sum
            else:
                return [leftPtrIndex+1, rightPtrIndex+1]