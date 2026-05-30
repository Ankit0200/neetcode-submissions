class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=1
        bypass_prod=1
        counter=0
        for char in nums:
            if char!=0:
                products=products * char
            else:
                bypass_prod=0
                counter+=1
        new_list=[]
        invalid=0

        if bypass_prod==1:
            for char in nums:
                new_list.append(int(products/char))
        else:
            for char in nums:
                if char!=0:
                    new_list.append(invalid)
                else:
                    if counter>=2:
                        new_list.append(invalid)
                    else:
                        new_list.append(products)
                
        return new_list

        

            
        