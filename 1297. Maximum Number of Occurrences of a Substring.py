class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res=[]
        windowsize=minSize
        while windowsize<maxSize+1:
            slidingWindowCount=len(s)-windowsize+1
            index=0
            while slidingWindowCount>0:
                unq=[]
                tmpstr=s[index:windowsize+index]
                c=0
                c=len(set(tmpstr))
                if c<=maxLetters:
                    res.append(tmpstr)
                index+=1
                slidingWindowCount-=1
            windowsize+=1
        x=Counter(res)
        if x:
            ma = max(zip(x.values(), x.keys()))[0]
            return ma
        else:
            return 0

