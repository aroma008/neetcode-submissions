class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ns={}
        for i in range(len(strs)):
            word=strs[i]
            s_word=''.join(sorted(word))
            if s_word not in ns:
                ns[s_word]=[word]
            else:
                ns[s_word].append(word)
        return list(ns.values())   

            

        