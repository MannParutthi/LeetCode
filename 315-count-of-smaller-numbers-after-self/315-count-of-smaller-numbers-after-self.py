class Solution:
    def merge(self, count, arr, left, mid, right): #arrays are merged here to get the result in descending order - reverse sorted
        temp = [] # temp array which stores the merged list made out of two sorted list arr[left:mid] & arr[mid+1:right]
        i = left  # i is pointer of arr[left:mid] - arr is sorted as [10,8,6,4,2] reverse order
        j = mid+1 # j is pointer of arr[mid+1:right] - arr is sorted as [9,7,5,3,1] reverse order
        
        while i<=mid and j<=right:
            if arr[i][0] <= arr[j][0]: # arr[x][0] = value & arr[x][1] = index 
                temp.append(arr[j])
                j += 1
            else: # i > j - as both arr are sorted individually - so all ele after j till end of arr will be smaller than arr[i]
                count[arr[i][1]] += right - j + 1 # main logic - no of ele between j and right including both of them 
                temp.append(arr[i])
                i += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= right:
            temp.append(arr[j])
            j += 1
            
        arr[left : right+1] = temp # copy the merged sorted list into the original array 
    
    
    def mergeSort(self, count, arr, left, right):
        if left < right:
            mid = left + (right-left) // 2
            self.mergeSort(count, arr, left, mid)
            self.mergeSort(count, arr, mid+1, right)
            self.merge(count, arr, left, mid, right)

            
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        arr = [[value, index] for index, value in enumerate(nums)] # arr[i][0] = value & arr[i][1] = index 
        
        self.mergeSort(count, arr, 0, len(nums)-1)
        return count