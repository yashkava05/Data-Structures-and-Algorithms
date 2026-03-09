class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # using two maps to map each char from strings 1 and 2 to each other
        map_s_t = {}
        map_t_s = {}

        # looping through the strings to map
        for i in range(len(s)):
            c1 = s[i] # char one variable of the first string
            c2 = t[i]

            if ((c1 in map_s_t and map_s_t[c1] != c2) or (c2 in map_t_s and map_t_s[c2] != c1)):
                return False
            map_s_t[c1] = c2
            map_t_s[c2] = c1

        return True
