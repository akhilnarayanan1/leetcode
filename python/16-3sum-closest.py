class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        min_sum = float('inf')                                      # Setting min_num to maximum number
        size = len(nums)
        
        nums.sort()                                                 # Sorting necessary for binary search
        
        ans = 0
        
        for first in range(0, size-2):

            second = first + 1
            third = size - 1                                        # Setting second and third index

            while second < third:
                total = nums[first] + nums[second] + nums[third]    # Get total of elements from 3 indexes
                diff = abs(target - total)

                if diff == 0:
                    return total                                    # Return as soon as total == target
                
                if diff < min_sum:
                    min_sum = diff
                    ans = total
                
                if total < target:
                    second += 1
                else:
                    third -= 1                                      # Binary search
        
        return ans
                
                
            
        