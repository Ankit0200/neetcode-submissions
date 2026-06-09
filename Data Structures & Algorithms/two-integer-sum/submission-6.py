class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for char in nums:
            next_val=target-char

            if next_val in nums[nums.index(char):]:
                second_index=nums.index(next_val)
                first_index=nums.index(char)
                my_list=[first_index,second_index]
                return my_list

