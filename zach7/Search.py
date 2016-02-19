#Search by Zachary Robinson
from collections import deque
import sys

#Classes to build graph
class GraphNode:
    parent = -1
    def __init__(self, name):
        self.name = name
        self.edgeList = []
    def addEdge(self, node, weight):
        edge = GraphEdge(node, weight)
        self.edgeList.append(edge)
    def searchParent(self, node):
        self.parent = node
class GraphEdge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

#breadth first search algorithm expects (list, GraphNode, string)
def breadthFirst(graph, start, end):
    path = []
    if start.name == end:
        path.append(start.name)
        return path
    else:
        queue = deque()
        visited = []
        queue.append(start)
        
        while queue:
          
            currentNode = queue.popleft()
            visited.append(currentNode.name)
            if currentNode.name == end:
                path.append(currentNode.name)
                while not currentNode.parent == -1:
                    path.append(currentNode.parent.name)
                    currentNode = currentNode.parent
                return path
            if not len(currentNode.edgeList) == 0:
                
                for i in currentNode.edgeList:
                    check = 0
                    for k in visited:
                        if k == i.node:
                            check = 1
                    for j in graph:
                        if j.name == i.node and check == 0:
                            j.searchParent(currentNode)
                            queue.append(j)
    return ''
#depth first search algorithm expects (list, GraphNode, string)
def depthFirst(graph, start, end):
    path = []
    if start.name == end:
        path.append(start.name)
        return path
    else:  
        stack = []
        visited = []
        stack.append(start)
        
        while stack:
            currentNode = stack.pop()
            visited.append(currentNode.name)
            if currentNode.name == end:
                path.append(currentNode.name)
                while not currentNode.parent == -1:
                    path.append(currentNode.parent.name)
                    currentNode = currentNode.parent
                return path
            if not len(currentNode.edgeList) == 0:
                for i in currentNode.edgeList:
                    check = 0
                    for k in visited:
                        if k == i.node:
                            check = 1
                    for j in graph:
                        if j.name == i.node and check == 0:
                            j.searchParent(currentNode)
                            stack.append(j)
    return ''
#uniform cost search algorithm expects (list, GraphNode, string)
def uniformCost(graph, start, end):
    path = []
    if start.name == end:
        path.append(start.name)
        return path
    else:
        queue = deque()
        visited = []
        distances = []

        for i in graph:
            if i.name == start.name:
                distances.append([i.name, 0])
            else:
                distances.append([i.name, 999999999])

        queue.append(start)
        
        while queue:
            
            currentNode = queue.popleft()
            visited.append(currentNode.name)
            tempDist = 0
            for j in distances:
                if j[0] == currentNode.name:
                    tempDist = j[1]
            if currentNode.name == end:
                
                path.append(currentNode.name)
                while not currentNode.parent == -1:
                    
                    path.append(currentNode.parent.name)
                    currentNode = currentNode.parent
                    
                return path
            if not len(currentNode.edgeList) == 0:
                for i in currentNode.edgeList:
                    for j in distances:
                        if j[0] == i.node:
                            if (i.weight + tempDist) < j[1]:
                                j[1] = i.weight + tempDist
                                for k in graph:
                                    if k.name == i.node:
                                        k.searchParent(currentNode)
            leastDist = -1
            nextNode = 0
            for i in distances:
                if leastDist == -1:
                    for j in graph:
                        check = 0
                        if j.name == i[0]:
                            for k in visited:
                                if k == j.name:
                                    check = 1
                            if check == 0:
                                nextNode = j
                                leastDist = i[1]
                else:
                    if i[1] < leastDist:
                        for j in graph:
                            if j.name == i[0]:
                                for k in visited:
                                    if k == j.name:
                                        check = 1
                                if check == 0:
                                    nextNode = j
                                    leastDist = i[1]
            if not nextNode == 0 and not leastDist == 999999999:
                queue.append(nextNode)
    return ''               
            
            
nodes = []
try:
    inFile = open(sys.argv[1], 'r')
    for line in inFile:
        thisLine = line.split(' ')
        check1 = 0
        check2 = 0
        for i in nodes:
            if i.name == thisLine[0]:
                check1 = 1
        for i in nodes:
            if i.name == thisLine[1]:
                check2 = 1
        if check2 == 0:
            newNode = GraphNode(thisLine[1])
            nodes.append(newNode)
        if check1 == 0:
            newNode = GraphNode(thisLine[0])
            newNode.addEdge(thisLine[1], int(thisLine[2]))
            nodes.append(newNode)
           
        else:
            for i in nodes:
                if i.name == thisLine[0]:
                    i.addEdge(thisLine[1], int(thisLine[2]))
   
    outFile = open(sys.argv[2], 'w')
    
    for i in nodes:
        if i.name == sys.argv[3]:
            if sys.argv[5] == 'BFS':
                path = breadthFirst(nodes, i, sys.argv[4])
                if not len(path) == 0:
                    path.reverse()
                
                for j in path:
                    outFile.write(j)
                    outFile.write('\n')
            elif sys.argv[5] == 'DFS':
                path = depthFirst(nodes, i, sys.argv[4])
                if not len(path) == 0:
                    path.reverse()
                
                for j in path:
                    outFile.write(j)
                    outFile.write('\n')
            elif sys.argv[5] == 'UCS':
                path = uniformCost(nodes, i, sys.argv[4])
                if not len(path) == 0:
                    path.reverse()
                 
                for j in path:
                    outFile.write(j)
                    outFile.write('\n')
   
    
except ValueError:
    print ('Error')

