class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        check = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            check[s[i]] = check.get(s[i],0) +1
            check[t[i]] = check.get(t[i],0) -1
        for val in check.values():
            if val != 0:
                return False
        return True


        