class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window problem
        seen= set()
        max_len = 0
        left = 0

        #s="abcabcbb" -> seen ={}


        for right in range(len(s)):

            while s[right] in seen:
                #right =3 so a is again. 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right]) 
            max_len = max(max_len, right - left + 1)
        
        return max_len
        





            