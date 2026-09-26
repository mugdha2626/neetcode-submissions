class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right =len(nums) - 1
        ans = -1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # if the left half is sorted: is it normally sorted if smaller than mid
            #if it is, then is it in between the left and the mid then
            #if not then we need to go to the right side

            #if the right side is sorted, we will w
            if nums[left] <= nums[mid]:
                #left half is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                #right half is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return ans
        