class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        i=1
        idx=0
        while n>0 and idx<len(target):
            if target[idx]==i:
                res.append("Push")
                idx+=1
            else:
                res.append("Push")
                res.append("Pop")
            n-=1
            i+=1
        return res
