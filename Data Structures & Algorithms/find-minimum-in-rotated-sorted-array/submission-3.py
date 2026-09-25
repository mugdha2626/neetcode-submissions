class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1


        while left < right:

            mid = left + (right - left) // 2

            #atleast two of the three, the left, middle or the right will be int he same sorted sub array
            #[4,5,0,1,2,3]

            # If middle element is greater than rightmost element, 
            # the minimum is guaranteed to be in the right half.

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        
        return nums[left]