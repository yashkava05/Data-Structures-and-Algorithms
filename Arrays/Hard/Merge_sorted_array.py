class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # using three pointers
        size = m+n
        index = size-1 # end of the nums1
        i = m-1 # end of numbers of the nums1
        j = n-1 # end of the nums2

        # starting from the end of both lists
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1


        # copying remaining elements from nums2
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
            
