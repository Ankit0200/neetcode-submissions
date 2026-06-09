class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict=dict()
       
        for char in nums:
            my_list=[]
            next_val=target-char
            my_list.append(nums.index(char))

            if next_val in nums and next_val!= char:
                my_list.append(nums.index(next_val))
                return my_list
                
            elif next_val == char:
                nums.remove(my_list.index(next_val))

            if next_val in nums:
                my_list.append(nums.index(next_val))
            return my_list
            
            
            
                
        
