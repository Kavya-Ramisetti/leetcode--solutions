class Solution:
    def sumGame(self, num: str) -> bool:
        lefts,rights,lq,rq=0,0,0,0
        n=len(num)
        h=n//2
        for i in range(h):
            if num[i]=='?':
                lq+=1
            else:
                lefts+=int(num[i])
        for i in range(h,n):
            if num[i]=='?':
                rq+=1
            else:
                rights+=int(num[i])
        diff=lefts-rights
        #if(diff==0 and lq==rq):
            #return False
        #else:
        #tar=(lq-rq)*9/2
        return 2*diff!=-9*(lq-rq)
