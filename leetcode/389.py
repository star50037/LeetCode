class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #2.7 3.5
        s = list(s)
        t = list(t)
        for i in s:
            t.remove(i)
        return(t[0])
        
        
        