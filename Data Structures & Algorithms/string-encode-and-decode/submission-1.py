class Solution:

    def encode(self, strs: List[str]) -> str:
        ns=''
        for i in strs:
            num=len(i)
            ns+=str(num)+'#'+i
        
            
        return ns

    def decode(self, ns: str) -> List[str]:
        rs=[]
        i=0
        while i<len(ns):
            j=ns.find('#',i)
            l=int(ns[i:j])
            w=ns[j+1:j+l+1]
            rs.append(w)
            i=j+1+l
        return rs
