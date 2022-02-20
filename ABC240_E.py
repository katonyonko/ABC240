import io
import sys

_INPUT = """\
6
3
2 1
3 1
5
3 4
5 4
1 2
1 4
5
4 5
3 2
5 2
3 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def EulerTour(G, s):
    res=[[0,0] for _ in range(len(G))]
    tmp=1
    depth=[-1]*len(G)
    depth[s]=0
    done = [0]*len(G)
    Q = [~s, s] # 根をスタックに追加
    parent=[-1]*len(G)
    ET = []
    left=[-1]*len(G)
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            if left[i]==-1: left[i]=len(ET)
            ET.append(i)
            res[i][0]=tmp
            if len(G[i])==1 and G[i][0]==parent[i]: tmp+=1
            for a in G[i][::-1]:
                if done[a]: continue
                depth[a]=depth[i]+1
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        else: # 帰りがけの処理
            ET.append(parent[~i])
            res[~i][1]=tmp-1
    return res
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N-1):
    u,v=map(int,input().split())
    u-=1; v-=1
    G[u].append(v)
    G[v].append(u)
  res=EulerTour(G, 0)
  for i in range(N):
    print(*res[i])