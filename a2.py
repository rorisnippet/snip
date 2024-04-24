class Node:

    def __init__(self, f=0, g=999999, h=0, name=0):
        self.f = f
        self.g = g
        self.h = h
        self.name = name
    
    def setNeighbours(self, neighbours={}):
        self.neighbours = neighbours


# assume a 5 node bidirectional graph as follows
graph = [ 
          [-1,  1, -1, -1, -1, 12],
          [1,  -1,  2,  1, -1, -1],
          [-1,  2, -1, -1,  5, -1],
          [-1,  1, -1, -1,  3,  4],
          [-1, -1,  5,  3, -1,  2],
          [12, -1, -1,  4,  2, -1]
         ]


# assume heuristics for each node
heuristics = [5,3,4,2,6,0]

s = Node(h=heuristics[0], name=0)
a = Node(h=heuristics[1], name=1)
b = Node(h=heuristics[2], name=2)
c = Node(h=heuristics[3], name=3)
d = Node(h=heuristics[4], name=4)
g = Node(h=heuristics[5], name=5)


s.setNeighbours([a,g])
a.setNeighbours([c, b])
b.setNeighbours([a, d])
c.setNeighbours([a, d, g])
d.setNeighbours([b, c, g])
g.setNeighbours([s, c, d])

startNode = s
goalNode = g


def astar(start,goal):

    closedSet = set([])
    openSet = set([start])

    cameFrom = {}
    
    start.g = 0
    start.f = start.h

    while len(openSet) != 0:

        current = findNodeWithLowestFScore(openSet)

        if current == goal:
            return construct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        for neighbour in current.neighbours:

            if neighbour in closedSet:
                continue

            if neighbour not in openSet:
                openSet.add(neighbour)

            tentative_gScore = current.g + graph[current.name][neighbour.name]

            if tentative_gScore >= neighbour.g:
                continue

            cameFrom[neighbour] = current
            neighbour.g = tentative_gScore
            neighbour.f = neighbour.g + neighbour.h

    return -1

def findNodeWithLowestFScore(openSet):
    fScore = 999999
    node = None
    for eachNode in openSet:
        if eachNode.f < fScore:
            fScore = eachNode.f
            node = eachNode

    return node

def construct_path(cameFrom, current):
    totalPath = []
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.append(current)

    return totalPath


if __name__ == "__main__":
    path = astar(startNode, goalNode)

    print("Path is: ", end="")
    for node in path[::-1]:
        print(str(node.name) + "-->", end="")
    print(goalNode.name)

    print("\nCost =", str(goalNode.g))

class Node:
    def __init__(self, f=0, h=0, name=0):
        self.f = f
        self.h = h
        self.name = name
    
    def setNeighbours(self, neighbours=[]):
        self.neighbours = neighbours



# Assume heuristics for each node
heuristics = [7, 8, 4, 3, 6,2,0]

s = Node(h=heuristics[0], name=0)
a = Node(h=heuristics[1], name=1)
b = Node(h=heuristics[2], name=2)
c = Node(h=heuristics[3], name=3)
d = Node(h=heuristics[4], name=4)
e = Node(h=heuristics[5], name=5)
g = Node(h=heuristics[6], name=6)

s.setNeighbours([a, b])
a.setNeighbours([s,d,c])
b.setNeighbours([s,c,e])
c.setNeighbours([a,b])
d.setNeighbours([a])
e.setNeighbours([b,g])
g.setNeighbours([e])

startNode = s
goalNode = g

def best_first_search(start, goal):
    closedSet = set([])
    openSet = set([start])
    cameFrom = {}

    while len(openSet) != 0:
        current = findNodeWithLowestFScore(openSet)

        if current == goal:
            return construct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        for neighbour in current.neighbours:
            if neighbour in closedSet:
                continue

            if neighbour not in openSet:
                openSet.add(neighbour)

            cameFrom[neighbour] = current

    return -1

def findNodeWithLowestFScore(openSet):
    fScore = 999999
    node = None
    for eachNode in openSet:
        if eachNode.h < fScore:
            fScore = eachNode.h
            node = eachNode

    return node

def construct_path(cameFrom, current):
    totalPath = []
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.append(current)

    return totalPath

if __name__ == "__main__":
    path = best_first_search(startNode, goalNode)

    print("Path is: ", end="")
    total_cost = 0
    for node in path[::-1]:
        print(str(node.name) + "-->", end="")
        total_cost += node.h  # Corrected from node.f to node.h
    print(goalNode.name)

    print("\nTotal Heuristic Cost =", str(total_cost))
