import io
import sys

_INPUT = """\
6
2 10
3 6
4 5
2 10
10 100
10 100
4 12
1 8
5 7
3 4
2 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  r=[0]*10001
  r[0]=1
  for i in range(N):
    a,b=map(int,input().split())
    tmp=[0]*10001
    for j in range(10001):
      if r[j]==1:
        if j+a<10001:
          tmp[j+a]=1
        if j+b<10001:
          tmp[j+b]=1
    r=tmp
  if r[X]==1:
    print('Yes')
  else:
    print('No')