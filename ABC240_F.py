import io
import sys

_INPUT = """\
6
4
3 7
-1 2
2 3
-3 2
10 472
-4 12
1 29
2 77
-1 86
0 51
3 81
3 17
-2 31
-4 65
4 23
1 1000000000
4 1000000000
2 5
-1 3
-2 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]
    ans=-(10**100)
    tmp=0
    now=0
    for i in range(N):
      x,y=a[i]
      if tmp>0 and x<0 and tmp//(-x)<=y:
        k=tmp//(-x)
        ans=max(ans,now+k*tmp+k*(k+1)//2*x)
      ans=max(ans,now+tmp+x)
      now+=y*tmp+y*(y+1)//2*x
      ans=max(ans,now)
      tmp+=x*y
    print(ans)