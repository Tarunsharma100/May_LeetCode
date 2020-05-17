class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row,col=len(image), len(image[0])
        colour=image[sr][sc]
        
        if colour==newColor:
            return image
        def dfs(r,c):
            if image[r][c]==colour:
                image[r][c]=newColor
                if r>=1: dfs(r-1,c)
                if r+1 < row :dfs(r+1,c)
                if c>= 1: dfs(r,c-1)
                if c+1 < col: dfs(r,c+1)
        dfs(sr,sc)
        return image
            