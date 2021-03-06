class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total_sum =0
        max_ending_at=0
        min_ending_at=0
        max_sum =-sys.maxsize-1
        min_sum= sys.maxsize

        for x in A:
	        total_sum +=x
	        max_ending_at=max(max_ending_at + x,x)
	        max_sum=max(max_ending_at,max_sum)
	        min_ending_at=min(min_ending_at + x,x)
	        min_sum=min(min_ending_at,min_sum)

        if(max_sum >0):
		    return max(max_sum,total_sum-min_sum)
        return max_sum		
        