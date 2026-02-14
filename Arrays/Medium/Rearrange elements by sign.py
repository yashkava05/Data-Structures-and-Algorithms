class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Brute force - Using two different arrays to store the positive and negative numbers respectively.
        positives = []
        negatives = []

        #If num is positive - adding to positives array, same with negative
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)


        #Creating a new results array to store the numbers alternately.
        results = []

        n = len(positives)

        for i in range(n):
            results.append(positives[i])
            results.append(negatives[i])

        return results

#Optimal approach

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Using two pointers to track the positive and negative numbers.
        i = 0
        j = 1
        #Creating a results array
        result = [0] * n

        #Iterating through the array to look for +ves and -ves
        for k in range(n):
            if nums[k] > 0:
                #If +ve, directly copying it to the results array.
                result[i] = nums[k]
                #Shifting i to the next positive index
                i += 2
            if nums[k] < 0:
                result[j] = nums[k]
                #Shifting j to the next negative index.
                j += 2

        return result
