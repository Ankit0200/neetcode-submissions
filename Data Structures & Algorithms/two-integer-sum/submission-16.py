class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for char in nums:
            diff=target-char
            my_list=[]
            if diff in nums[(nums.index(char)+1):]:
                first_index=nums.index(char)
                second_index=nums.index(diff)

                my_list.append(first_index)
                my_list.append(second_index)
                return my_list


       
      
                
        
