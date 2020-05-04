class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=bin(num).replace("0b","")
        ns=""
        for i in range(len(n)):
    
            print(n[i])
            if n[i]=='0':
                print(n[i])
                ns=ns+str(1)
            else:
                ns=ns+str(0)
                
        return int(ns,2)