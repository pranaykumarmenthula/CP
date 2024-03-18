class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count=0
        properties=sorted(properties,key=lambda x: (-x[0],x[1]))
        maxDefance=properties [0][1]
        for i in properties:
            if i[1]<maxDefance:
                count+=1
            maxDefance=max(i[1],maxDefance)
        return count
