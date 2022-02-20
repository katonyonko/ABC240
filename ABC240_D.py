import io
import sys

_INPUT = """\
6
5
3 2 3 2 2
10
2 3 2 3 3 3 2 3 3 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N=int(input())
  A=list(map(int,input().split()))
  dq=deque()
  for i in range(N):
    if len(dq)>0 and dq[-1][0]==A[i]:
      if dq[-1][1]==dq[-1][0]-1:
        for j in range(dq[-1][0]-1):
          dq.pop()
      else:
        dq.append([A[i],dq[-1][1]+1])
    else:
      dq.append([A[i],1])
    print(len(dq))