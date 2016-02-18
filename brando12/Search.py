#Graph Search
#Brandon Walsh (brando12@umbc.edu)
#CMSC 471: AI
#2/15/16
import sys

#=================MAIN================
def main():

    #Get input from user
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    sNode = sys.argv[3]
    eNode = sys.argv[4]
    sType = sys.argv[5]

    #Create the Graph the input
    graph = Graph(inFile,outFile)

    #Call the specific graph
    try:
        if sType == "DFS":
            graph.dfs(sNode,eNode)

        elif sType == "BFS":
            graph.bfs(sNode,eNode)

        elif sType == "UCS":
            graph.ucs(sNode,eNode)
    except KeyError:
        print ("Node Not Found")
        f = open(outFile, 'w')
        f.write("")
    except IndexError:
        print ("Node Not Found")
        f = open(outFile, 'w')
        f.write("")
#======================================


#==============GRAPH CLASS=============
class Graph:

    def __init__(self,inFile,outFile):
        self.inFile = inFile
        self.outFile = outFile
        self.nodes = {} #stores nodes

        #open input file
        file = open(inFile, 'r')
        lines = (file.readlines())

        #loop input & generate nodes
        for line in lines:
            line = line.replace("\n","").split()

            #Retrieve or create parent node
            parent = Node("");
            if line[0] in self.nodes:
                parent = self.nodes.get(line[0])
            else:
                parent = Node(line[0])

            #retrieve or create child node
            child = Node("");
            if line[1] in self.nodes:
                child = self.nodes.get(line[1])
            else:
                child = Node(line[1])

            #Append child node to parent
            #Also append the edge weight
            parent.addChild(child,line[2])

            #Update the nodes list
            self.nodes.update({line[0]:parent})
            self.nodes.update({line[1]:child})


    #======== DEPTH FIRST SEARCH ========
    def dfs(self,start,end):

        #initialize variables
        stack = Stack()
        currentNode = self.nodes[start]
        endNode = self.nodes[end]
        stack.push(currentNode)

        #start searching
        found = False;
        while found == False:

            #Check top of stack for node
            currentNode = stack.peek()

            #Mark node as visited
            currentNode.visited = True;

            #end loop if node found
            if currentNode is endNode:
                found = True;

            #if the current node has children
            elif currentNode.numChildren > 0:

                tracker = currentNode.childTracker

                if tracker == currentNode.numChildren:
                    stack.pop()
                else:
                    stack.push(currentNode.children[tracker])
                    currentNode.childTracker = tracker + 1

            #if the node has no children pop
            elif currentNode.numChildren == 0:
                stack.pop()

        stack.test()

        self.__results(stack.items)

    #=========BREADTH FIRST SEARCH==========
    def bfs(self,start,end):

        #initialize variables
        queue = Queue()
        currentNode = self.nodes[start]
        endNode = self.nodes[end]
        queue.add(currentNode)
        currentNode.path.append(currentNode)

        #start searching
        found = False;
        while found == False:

            #Check top of stack for node
            currentNode = queue.peek()

            #Mark node as visited
            currentNode.visited = True;

            #end loop if node found
            if currentNode is endNode:
                found = True;

            else:
                for child in currentNode.children:
                    queue.add(child)

                    #update path
                    newPath = list(currentNode.path)
                    newPath.append(child)
                    child.path = newPath

                queue.pop()

        for n in endNode.path:
            print (n.name)

        self.__results(endNode.path)

    #==========UNIFORM COST SEARCH=============
    def ucs(self,start,end):

        #initialize variables
        currentNode = self.nodes[start]
        endNode = self.nodes[end]
        currentNode.path.append(currentNode)
        options = [currentNode]

        #start searching
        found = False;
        while found == False:

            #end loop if node found
            if currentNode is endNode:
                found = True;

            else:

                #sort the node options
                options.sort(key = lambda x: x.totalWeight)

                #print (currentNode.name)
                #get the lowest cost node
                currentNode = options[0]

                #parse children
                c = 0
                for child in currentNode.children:

                    #create a new weight for the next node
                    newWeight = currentNode.totalWeight + currentNode.weight[c]

                    #see if the new weight is cheaper or the child hasnt been reached
                    if (child.totalWeight > newWeight) or (child.totalWeight == 0):

                        child.totalWeight = newWeight

                        options.append(child)

                        #Set the new path
                        newPath = list(currentNode.path)
                        newPath.append(child)
                        child.path = newPath

                    c += 1

                #remove the traversed node from options
                options.pop(0)

        #print the test results
        for t in currentNode.path:
            print (t.name)

        #send the results to the output file
        self.__results(endNode.path)


    #Prints results in output file
    def __results(self,array):
        f = open(self.outFile, 'w')
        for item in array:
            f.write(item.name + "\n")


#===========NODE CLASS================
class Node:

    def __init__(self,name):
        self.name = name
        self.children = []
        self.weight = []
        self.totalWeight = 0
        self.numChildren = 0
        self.childTracker = 0
        self.visited = False;
        self.path = []


    def addChild(self,node,weight):
        self.children.append(node)
        self.weight.append(int(weight))
        self.numChildren = self.numChildren + 1


#=========STACK CLASS============
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def test(self):
         for item in self.items:
             print (item.name)

#==========QUEUE CLASS=============
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def test(self):
        for item in self.items:
            print (item.name)


main()
