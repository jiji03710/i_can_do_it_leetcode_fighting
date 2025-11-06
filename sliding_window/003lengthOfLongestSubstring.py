class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordlist={}
        start = 0
        max_len=0
        
        for end in range(len(s)):
            if s[end] in wordlist and wordlist[s[end]]<end:
                start = wordlist[s[end]]+1
            wordlist[s[end]]=end
            max_len = max(max_len, end-start+1)
        return max_len
