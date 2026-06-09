class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for char in nums:
            next_val=target-char
            first_index=nums.index(char)
            my_list=[]
            my_list.append(first_index)

            if next_val in nums:
                print("WtF")
                second_index=nums.index(next_val)
                if first_index == second_index:
                    pass 
                else:
                     my_list.append(second_index)
                     return my_list

