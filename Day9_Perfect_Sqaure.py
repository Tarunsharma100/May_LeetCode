class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        sum=0
        while sum < num:
            sum=sum+i
            if sum==num:
                return True
            i=i+2
        return False   