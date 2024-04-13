class Solution:
    def frequencySort(self, s: str) -> str:
        l=list(s)
        x=Counter(l)
        x=dict(sorted(x.items(),key=lambda item:item[1] ,reverse=True))
        t=''
        for k,v in x.items():
            t=t+v*k
        return t
