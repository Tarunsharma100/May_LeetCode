from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s=Counter(s)
        list_s=list(dict_s)
        uni_list=[]
        print(dict_s)
        pos=-1
        for i in range(len(list_s)):
            
            if dict_s.get(list_s[i])==1:
                uni_list.append(list_s[i])
                
        print(uni_list)
        print(s)
        
        for i in range(len(s)):
            if s[i] in uni_list:
                pos=i
                break
            else:
                pos=-1
        
        return pos
        
        