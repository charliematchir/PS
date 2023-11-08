size = 100
parent = [i for i in range(size)]


def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

# 위의 find 는 p의 값이 바로 위 부모이지만
# 아래의 find는 p 값이 모두 root로 동일
# 길게 늘어서는 트리의 구조를 노드가 루트 아래에 위치하도록 만들어 트리의 높이를 작게하는것
# Path Compression, Union By Rank


def Optfind(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x


rank = [0] * size
def RankUnion(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
