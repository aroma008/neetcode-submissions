class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        o={}
        for i in nums:
            if i in o:
                o[i]+=1
            else:
                o[i]=1
                
        s=sorted(o,key=o.get,reverse=True)
        n=s[:k]
        return n

        
        