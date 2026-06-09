class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        for char in range(len(nums)):
            if target-nums[char] in nums:
                if nums.index(target-nums[char])!=nums[char]:
                    my_list =[char,nums.index(target-nums[char])]
                    return my_list
