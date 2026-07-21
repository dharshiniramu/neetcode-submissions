class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1="".join(sorted(s1))
        
        left=0
        right=len(s1)-1
        while right < len(s2):
            text="".join(sorted(s2[left:right+1]))
            print(text)
            if sorted_s1==text:
                return(True)
            left+=1
            right+=1
        return(False)
        