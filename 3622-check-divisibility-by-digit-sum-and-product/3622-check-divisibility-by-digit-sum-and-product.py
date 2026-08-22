import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits=list(map(int,str(n)))
        s=sum(digits)
        p=math.prod(digits)
        return n%(s+p)==0