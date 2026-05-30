class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)==len(t):
        new_list=[]
        for char in s:
            new_list.append(char)
        for char in t:
            if char in new_list:
                new_list.remove(char)
            else:
                break
        if (len(new_list)==0):
            return True
        else:
            return False
      else:
        return False
            
        