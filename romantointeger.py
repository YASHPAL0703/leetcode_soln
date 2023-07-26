class Solution:
    def romanToInt(self, s: str) -> int:
        rnm_list={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)
        ans=0
        for i in range(0,l):
            if  i<l-1 and rnm_list[s[i]]<rnm_list[s[i+1]] :
                ans-=rnm_list[s[i]]
            else:
                ans+=rnm_list[s[i]]
        return ans
