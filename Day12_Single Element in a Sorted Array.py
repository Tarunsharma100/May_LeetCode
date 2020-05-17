from collections import Counter
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict=Counter(nums)
        d_list=list(dict)
        
        for i in range(len(d_list)):
            
            if dict.get(d_list[i])==1:
                key=d_list[i]
                
            
        return key 