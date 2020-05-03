from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        count=0
        
        JJ = Counter(J) 
        SS = Counter(S) 
       
        
        JJ_list=list(JJ.keys())
        SS_list=list(SS.keys())
        
        
      
        for i in range(len(JJ_list)):
            
            if JJ_list[i] in SS_list:
                
                count=count+SS.get(JJ_list[i])
               
     
                   
       
        return count



        