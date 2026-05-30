class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen ={}
        for char in strs:
            ascii_values=[str(ord(letter)) for letter in char]
            ascii_values.sort()
            key="".join(ascii_values)

            if key in seen:
                seen[key].append(char)
            else:
                seen[key]=[char]
        returning_list=[]
        for value in seen.values(): 
            returning_list.append(value)
        return returning_list

       
        