class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        
        left = 0

        maxno = 0
        max_freq = 0

        for right in range (len(s)):

            #update the freq of the char we have

            freq[s[right]] = freq.get(s[right],0) +1
            #the max freq updates now
            max_freq = max(freq.values())

            #the num of char we can replace are greater than k, then we need to skrink the window. we need the min window such that we can get all the k
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left +=1 
            maxno = max(maxno, right-left +1)
        return maxno