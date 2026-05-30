class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1

        run_loop=True

        while run_loop:
            our_val=numbers[start]+numbers[end]

            if our_val<target:
                start=start+1
            elif our_val>target:
                end=end-1
            
            else:
                if start==end:
                    pass
                else:
                    my_list=[start+1,end+1]

                    return my_list



