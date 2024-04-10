class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        windowSize=3
        slidingWindowCount=len(s)-windowSize+1
        index=0
        c=0
        while slidingWindowCount>0:
            lst=[]
            tmpstr=s[index:windowSize+index]
            for i in tmpstr:
                if i in lst:
                    break
                else:
                    lst.append(i)
            else:
                c+=1
            index+=1
            slidingWindowCount-=1
        return c
