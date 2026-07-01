class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for j in range(k):
            l.append(sorted_dict[j][0])
        return(l)



        