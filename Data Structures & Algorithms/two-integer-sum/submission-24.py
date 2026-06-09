
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for char in nums:
            diff=target-char
            my_list=[]
            if diff in nums:
                
                print("came here")
                first_index=nums.index(char)
                second_index=nums.index(diff)
                if first_index==second_index:
                    second_index=nums.index(diff, nums.index(diff)+1)

                my_list.append(first_index)
                my_list.append(second_index)
                return my_list


       
      
                
        


       
      
                
        
