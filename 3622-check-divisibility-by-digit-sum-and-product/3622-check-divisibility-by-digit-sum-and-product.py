import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        o=n
        s=0
        p=1
        while n>0:
            rem=n%10
            s+=rem
            p*=rem
            n=n//10
        return o%(s+p)==0       

