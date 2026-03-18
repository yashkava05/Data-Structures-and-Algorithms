class Solution:
    # function to merge two sorted halves
    def merge(self, arr, low, mid, high):
        temp = []
        # taking two pointers to compare the sorted halves
        left = low
        right = mid + 1
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        # adding the remaining elements from either of the arrays
        while left <= mid:
            temp.append(arr[left])
            left += 1
            
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # copying the sorted temp into the og array.
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    # calling merge sort recursively
    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        # using mid to recursively divide the array
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)
        
# Driver code
arr = [5, 2, 8, 4, 1]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print(*arr)
