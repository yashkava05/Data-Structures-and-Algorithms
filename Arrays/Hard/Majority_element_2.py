# naive approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute using two for loops
        n = len(nums)

        result = []

        for i in range(n):
            if len(result) == 0 or result[-1] != nums[i]:

                count = 0

                for j in range(n):
                    if nums[j] == nums[i]:
                        count += 1

                if count > (n // 3):
                    result.append(nums[i])

            if len(result) == 2:
                break
        
        return result

# Optimal approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # using boyer-moore voting algorithm
        # we use two counters count1 and count2, and two numbers num1 and num2
        
        num1 = num2 = -1
        count1 = count2 = 0

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                num1 = num
            elif count2 == 0:
                count2 += 1
                num2 = num
            else: # if both arent equal we decrement
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        result = []
        if count1 > (n//3):
            result.append(num1)
        if count2 > (n//3):
            result.append(num2)

        return result
