class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin_index=0
        nums=numbers
        my_list=[]
        
        for char in nums:
            begin_index=0
            ending_index=len(nums)-1
            
            while begin_index<=ending_index:
                mp=(begin_index+ending_index)//2
                # print(mp)

                if char + nums[mp]==target:
                    my_list.append(char)
                    my_list.append(mp)
                    break
                elif char + nums[mp]<target:
                    begin_index=mp+1
                elif char + nums[mp]>target:
                    ending_index=mp-1
        
        if my_list:
            return [nums.index(my_list[0])+1,my_list[1]+1]


        