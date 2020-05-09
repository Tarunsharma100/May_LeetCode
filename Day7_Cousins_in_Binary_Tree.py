# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.pX=0
        self.pY=0
        self.dX=-1
        self.dY=-1
        
        self.parentAndDepth(root,x,y,0)
        return ((self.dX==self.dY) and (self.pX!=self.pY))
    
    def parentAndDepth(self,root,x,y,d):
        
        if(root==None):
            return
        
        # Left Tree
        if(root.left!=None):
            if(root.left.val==x):
                self.pX=root.val
                self.dX=d+1
                
            elif(root.left.val==y): 
                self.pY=root.val
                self.dY=d+1
        
        #Right Tree         
        if(root.right!=None):
            if(root.right.val==x):
                self.pX=root.val
                self.dX=d+1
                
            elif(root.right.val==y): 
                self.pY=root.val
                self.dY=d+1       
        if(self.dX!=-1 and self.dY!=-1):
            return
        
        self.parentAndDepth(root.left,x,y,d+1)
        self.parentAndDepth(root.right,x,y,d+1)
        