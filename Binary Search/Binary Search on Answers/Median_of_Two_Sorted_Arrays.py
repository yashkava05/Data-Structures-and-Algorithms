class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) +len(nums2)

        # we want only half of the elements on the left side of our partition.
        half = total // 2

        # binary searching on the smaller array for efficiency 0logmin(m, n)

        if len(A) > len(B):
            A, B = B, A

        left = 0
        right = len(A) - 1

        while True:
            # index of last element in A's partition
            i = (left + right) // 2
            # index of last element in B's partition.
            j = half - i - 2

            # using the four boundary middle values from both the arrays.
            # rightmost elem of A's left portion
            Aleft = A[i] if i >= 0 else float("-infinity")
            # leftmost elem of a's right
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            # rightmost elem of B's left
            Bleft = B[j] if j >= 0 else float("-infinity")
            # leftmost of B's right
            Bright = B[j + 1] if (j+1) < len(B) else float("infinity")

            # partition is correct when the left most values of both the arrays dont cross into the right part of the partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd total, median is the single midddle element ie. smaller of the two right side values
                if total % 2:
                    return min(Aright, Bright)
                # even total, avg of max of left half and min of right halves.
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                right = i - 1 # i is too far to the right, move partition left in A
            else:
                left = i + 1 # i is too far left, move partition right in A.
