class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count, counttwo = {}, {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            counttwo[t[i]] = 1 + counttwo.get(t[i], 0)

        return count == counttwo