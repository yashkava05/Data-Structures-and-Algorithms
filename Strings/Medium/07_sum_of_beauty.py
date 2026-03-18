class Solution:
    def beautySum(self, s: str) -> int:
        # using two pointers to check the characters and store the freq
        total = 0

        # outer loop to keep the pointer fixed
        for i in range(len(s)):
            freq = {}

            for j in range(i, len(s)):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1

                # calculating the beauty values.
                beauty = max(freq.values()) - min(freq.values())
                total += beauty

        return total
