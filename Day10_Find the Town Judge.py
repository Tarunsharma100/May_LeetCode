class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_count=[0]*N
        
        for i in trust:
            trust_count[i[0]-1]-=1
            trust_count[i[1]-1]+=1
        
        result=-1   
         
        for i in range(N):
            if trust_count[i]==N-1:
                return i+1
        return result    
            