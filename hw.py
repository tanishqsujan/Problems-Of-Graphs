from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.inCycle = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, recStack):
        visited.add(node)
        recStack.add(node)

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                if self.dfs(neighbour, visited, recStack):
                    self.inCycle.add(node)
                    return True
            elif neighbour in recStack:
                self.inCycle.add(node)
                self.inCycle.add(neighbour)
                return True

        recStack.remove(node)
        return False

    def findNodesNotInCycle(self):
        visited = set()
        for node in range(self.V):
            if node not in visited:
                self.dfs(node, visited, set())

        not_in_cycle = [node for node in range(self.V) if node not in self.inCycle]
        return not_in_cycle


g = Graph(6)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(3, 4)
g.addEdge(4, 5)

result = g.findNodesNotInCycle()
print("Nodes not part of any cycle:", result)
