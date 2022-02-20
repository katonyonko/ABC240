import io
import sys

_INPUT = """\
6
4 5
3 5
1 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a,b=map(int,input().split())
  if (a-1)%10==b%10 or a%10==(b-1)%10:
    print('Yes')
  else:
    print('No')