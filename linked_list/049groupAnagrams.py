class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap=defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            hashmap[sorted_word].append(word)
        return list(hashmap.values())