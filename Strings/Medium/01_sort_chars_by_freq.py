class Solution:
    def frequencySort(self, s: str) -> str:
        # using a counter to store each char's freq
        count = Counter(s)
        # higher freq comes first.
        sorted_chars = sorted(s, key = lambda x: (-count[x], x))
        return ''.join(sorted_chars)
