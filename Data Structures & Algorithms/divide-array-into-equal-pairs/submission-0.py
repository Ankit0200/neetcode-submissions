class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)
        if n%2==0:
            my_dict=defaultdict(int)
            for char in nums:
                my_dict[char]+=1
        print(my_dict)
        for char in my_dict:

            if my_dict[char]%2==0:
                pass
            else:
                return False
        return True

        