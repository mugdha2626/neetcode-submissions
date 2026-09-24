class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freq = {}
        #storing the freq of the char of the t
        for ch in t:
            freq[ch] = freq.get(ch,0) + 1
        
        need = len(freq)
        # need is unique values
        have = 0
        ans_bounds = [0,0]
        window = {}
        min_len = float('inf')
        left =0
        
        for right in range(len(s)):
            # add to the window
            window[s[right]] = window.get(s[right], 0) + 1
            # check if the window has all the stuff we need
            # check if that char is in the freq and then also the freq matches for both
            if s[right] in freq and freq[s[right]] == window[s[right]]:
                have += 1
            
            # if we find all the char we need
            while need == have:
                # we will start cutting char from the left

                #update the min window tracking
                # so if the current window is smaller than the overall min window we update. p standard. 
                if (right -left + 1) < min_len:
                    min_len = right - left + 1
                    ans_bounds = [left, right]
                
                #cut the left words
                window[s[left]] -= 1
                if s[left] in freq and window[s[left]] < freq[s[left]]:
                    #basically we need one more of that left char that we just cut off
                    have -= 1
                left += 1
        l, r = ans_bounds
        return s[l : r + 1] if min_len != float("inf") else ""
                




            
            
            
