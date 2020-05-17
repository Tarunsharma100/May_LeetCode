class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEndOfWord=False
        self.children=[None]*26
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self
        for c in word:
	        if((curr.children[ord(c)-ord('a')])==None):
		        curr.children[ord(c)-ord('a')]=Trie()
	        curr = curr.children[ord(c) - ord('a')]
        curr.isEndOfWord = True	                


        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr= self

        for c in word :
	        curr = curr.children[ord(c)-ord('a')]
	        if(curr == None):
		        return False    
        if (curr.isEndOfWord):
	            return True

        return False	

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for c in prefix :
	        curr =curr.children[ord(c)-ord('a')]
	        if(curr==None):
		        return False
        return True	



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)