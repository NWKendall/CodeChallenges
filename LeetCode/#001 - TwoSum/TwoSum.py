# iterate over list
# check value to be smaller than target
# save indeces
# return array of indeces that contain solution values

##### BRUTE FORCE #####
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute force approach - O(n^2)
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]

# RunTime = O(n^2) - nested loop
# Space = O(1) - always returning array with 2 elements
            
            
            