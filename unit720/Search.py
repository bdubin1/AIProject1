#run by: python Search.py <input file> <output file> <start node> <end node> <search_type>
def main():
    #create graph object
    graph = Graph()
    print (graph.search()) #search checks input and processes operations

if __name__ == "__main__":
    main()
    
#create node class
class Node:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = False
        self.distance = float('inf')
        self.parent = None
    
# create graph class
class Graph:
    def __init__(self):
        self.nodes = {}
        self.searchType = None
        
    #methods
    def getCommands():
        if len(sys.argv)==6:
            self.inFile = sys.argv[1]
            self.outFile = sys.argv[2]
            self.startNode = sys.argv[3]
            self.endNode = sys.argv[4]
            self.searchType = sys.argv[5]
            
    #readFile expects ((start,end),cost) split on each file line
    def readFile(inFile): # file input
        self.getCommands()
        with open (inFile, 'r') as file:
            for line in file:
                node = line.split(' ')
                self.addNode(node[0], node[1], node[2])
        
    def addNode(start, end, cost):
        node = Node(start, end, cost)
        self.nodes.append(node)

    def writeFile(outFile, output): # file output
        with open(outFile,'w') as file: #create file
            file.write(output)#write results
           
    def search(): #search by designated type
        self.readFile()
        self.output = ""
        if (searchType==None):
            self.output += "SearchError"
        elif (searchType=="BFS"):
            self.output += self.BFS(self, startNode)
        elif (searchType=="DFS"):
            self.output += self.DFS(self.startNode)
        elif (searchType=="UCS"):
            self.output += self.UCS(self.startNode)
        self.writeFile(self.outFile, self.output)
        
    def adjacentTo(other):
        if(other.end == self.start):#if self leads to other
            return True
        else:
            return False
    
    def getAdjacent(currentNode):#return nodes accessible from this node
        adjacent = {}
        for node in self.nodes:
            if other.adjacentTo(node):
                adjacent.append(node)
        return adjacent
    
    def BFS(startNode): #breadth-first-search (Graph, root)
        print ("BFS")
        from collections import deque
        queue = deque() #import & create empty queue Q
        for node in self.nodes: #for each node n in Graph
            node.distance = float('inf') #n.distance = INFINITY
            node.parent = None #n.parent = NIL
            if(startNode==node.start):
                node.distance = 0#root.distance = 0
                queue.append(node)#Q.enqueue(root)
        while(len(queue)>0):#while Q is not empty
            currentNode = queue.popleft()#current = Q.dequeue()
            for node in self.getAdjacent(currentNode):#for each node n that is adjacent to current:
                if(node.distance == float('inf')):#if n.distance == INF
                    node.distance = currentNode.distance + 1#n.distance = current.distance + 1
                    node.parent = currentNode.start#n.parent = current
                    queue.append(node)#Q.enqueue(n)
        return writeFile(self.outFile, self.output)
                
    def DFS(startNode):
        print ("DFS")
        for node in self.nodes:
            if (node.start == startNode):
                node.visited = True #label start as discovered
                break #already found the start
        for currentNode in getAdjacent(startNode):#for edges from v to w in G.adjacentEdges(v)
            if(currentNode.visited == False):#if node has not been visited
                self.DFS(currentNode)#recursively call DFS(G,W)
        return writeFile(self.outFile, self.output)
            
    def UCS(startNode): #uniform cost search
        print("UCS")
        #create vertex set Q
        from collections import deque
        queue = deque() 
        #for each vertex v in Graph:             // Initialization
        for node in self.nodes:
            #dist[v] ? INFINITY                  // Unknown distance from source to v
            if (node.start == startNode):
                node.distance = 0           #dist[source] ? 0
            else:
                node.distance = float('inf')
            #prev[v] ? UNDEFINED                 // Previous node in optimal path from source
            node.parent = None          
            queue.append(node)#add v to Q. All nodes initially in Q (unvisited nodes)
        while(len(queue)>0): #while Q is not empty:
            leastNode = None
            for node in self.nodes: #u ? vertex in Q with min dist[u] 
                if (leastNode == None) or (node.distance<leastNode.distance):
                    leastNode = node
            queue.remove(leastNode)#remove u from Q 
            for adjacent in self.getAdjacent(leastNode):#for adjacent nodes
                alternate = leastNode.distance + 1 #find length through leastNode
                if alternate < adjacent.distance:#if alt < dist[v], shorter path found
                    adjacent.distance = alternate #dist[v] ? alt 
                    adjacent.parent = leastNode.start #prev[v] ? u 
        #return dist[], prev[]
        return writeFile(self.outFile, self.output)