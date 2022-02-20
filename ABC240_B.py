import io
import sys

_INPUT = """\
6
6
1 4 1 2 2 1
1
1
11
3 1 4 1 5 9 2 6 5 3 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=set(list(map(int,input().split())))
  print(len(A))