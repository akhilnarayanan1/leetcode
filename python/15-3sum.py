import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()
        
        result = []
        
        for first in range(len(nums)-2):

            # Skip all duplicates from left ⏭️
            # first > 0 ensures this check is made only from 2nd element onwards
            
            if first > 0 and nums[first] == nums[first - 1]:
                continue
                
            second, third = first + 1, len(nums)-1
            
            while second < third:
                sum = nums[first]+nums[second]+nums[third]
                if sum == 0:

                    # Add triplet to result ⛓️
                    result.append((nums[first],nums[second],nums[third]))
                    third -= 1

                    # Skip all duplicates from right ⏭️
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                elif sum > 0:

                    # Decrement third to reduce sum value ⬇️
                    third -= 1
                else:

                    # Increment second to increase sum value ⬆️
                    second += 1
                    
            
        return result
            
        