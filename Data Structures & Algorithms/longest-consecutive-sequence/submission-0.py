class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_no = 0 

        #convert to a set to we have no duplicates
        #allows for o(1) lookups
        num = set(nums)

        #we check if the num is the first in the seq

        for n in num:

            streak = 0
            if (n - 1) not in num:
                streak = 1
                #this is the start of the seq

                while (n + 1) in num:
                    streak += 1
                    n += 1
                if streak > max_no:
                    max_no = streak

        return max_no