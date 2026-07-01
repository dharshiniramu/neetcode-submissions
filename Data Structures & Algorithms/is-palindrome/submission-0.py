class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=s.split()
        sn=''.join(l)
        ns=[]
        for i in sn:
            if i.isalnum():
                ns.append(i)
        ns2=ns.copy()
        
        l=0
        r=len(ns)-1
        while l<r:
            ns[l],ns[r]=ns[r],ns[l]
            l+=1
            r-=1
        print(ns2)
        print(ns)
        if ns==ns2:
            return True
        else:
            return False


        