#### 크루스칼 알고리즘 ####
# 비용이 적은순서대로 정렬한 뒤, 적은 순서대로 그래프에 포함
# 단, 사이클이 만들어지면 안됨

class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
        
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, root1, root2):
        # 연결정보를 갱신할 때는 작은 값을 기준으로 갱신
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
                

def solution(n, costs):
    minimum_weight = 0
    disjointset = DisjointSet(n)
    result = []
    for data in sorted(costs, key = (lambda cost : cost[2])):
        v, u, weight = data
        root1 = disjointset.find(v)
        root2 = disjointset.find(u)
        # root1 과 root2가 같은데 연결하면 사이클 생김
        if root1 != root2:
            disjointset.union(root1, root2)
            result.append(data)
            minimum_weight += weight
    
    return minimum_weight