class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        # print(nums)
        seen =set()

        for i,n in enumerate(nums):
            if n in seen:
               nums.remove(n)
            else:
                seen.add(n)
        print(nums)
        
        counter=1
        highest_counter=[]

        for key,values in enumerate(nums):
            if key < (len(nums)-1):
                if nums[key]+1==nums[key+1]:
                    counter+=1
                else:
                    highest_counter.append(counter)
                    counter=1
        
        highest_counter.append(counter)
        print(highest_counter)
        max_val=max(highest_counter)

        return max_val
        


        

        # counter=1
        # highest_counter=[]
        # my_dict=defaultdict()

        # for i,n in enumerate(nums):
        #     my_dict[i]=n
        # seen =set()
        
        # for key,values in my_dict.items():
        #     if values in seen:
        #         pass
        #     else:
        #         if key < (len(my_dict)-1):
        #             if my_dict[key]+1 == my_dict[key+1]:
        #                 counter+=1
        #             else:
        #                 highest_counter.append(counter)
        #                 counter=0
        #         highest_counter.append(counter)
        #         seen.add(values)
        
        # my_max=max(highest_counter)
        # return my_max
        