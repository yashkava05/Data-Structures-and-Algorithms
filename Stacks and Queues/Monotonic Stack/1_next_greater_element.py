class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using a stack to store the current greater element.
        stack = []

        # hashmap to map elements with their next greater element.
        nge_map = {}

        # traversing nums2 from left to right
        for num in nums2:
            # while stack is not empty and the current element is greater than the element at the top of the stack,
            while stack and stack[-1] < num:
                # this means that the top element has found its next greater, so we map it.
                nge_map[stack.pop()] = num

            # pushing current element onto the stack, it now waits for its own nge
            stack.append(num)

        # array to store the final result
        result = []

        for num in nums1:
            # checking if this element has a recorded nge in the map
            if num in nge_map:
                result.append(nge_map[num])
            else:
                result.append(-1)

        
        return result
