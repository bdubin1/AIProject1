##proj1
import sys
import queue
import heapq
inputFilename=sys.argv[1]
outputFilename=sys.argv[2]
startnode=sys.argv[3]
endnode=sys.argv[4]
searchType=sys.argv[5]
inputFile=open(inputFilename)
s=inputFile.read().split()
for i in range(2,len(s),3):
        s[i]=int(s[i])

d={}
counter=0
i=0
while len(s)-counter!=0:
	if s[counter] in d:
		d[s[counter]].update({s[counter+1]:s[counter+2]})
	else:
		d[s[counter]]={s[counter+1]:s[counter+2]}
	counter+=3
print(d)
inputFile.close()
graph=d

def bfs(graph, startnode, endnode):
    
    queue = []
    queue.append([startnode])
    while queue:
        
        path = queue.pop(0)
        
        node = path[-1]
        
        if node == endnode:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print(bfs(graph, startnode, endnode))


def dfs(graph, startnode, endnode):
	loopcount=0
	stack = []
	visited = []
	stack.append(startnode)
	if startnode== endnode:
		return visited
	print("stack:",stack)
	print("visited",visited)
	while stack:

		parent = stack.pop()
#		if parent in visited: 
#			continue
		if endnode==parent:
			visited.append(endnode)
			return visited
		visited.append(parent)
		node= visited[-1]
		children = graph.get(node,[])

		for child in children:
			stack.append(child[0])
			print("stack:",stack)
			print("visited",visited)

print(dfs(graph, startnode, endnode))

def ucs(graph, startnode, endnode):
	visited = set()
	q = [(0, ((),startnode))]
	while True:
		(cost, path) = heapq.heappop(q)
		state = path[-1]
		if not state in visited:
			visited.add(state)
			if state==endnode:
				return path
			for child in graph.get(state,[]):
				if child not in visited:
					heapq.heappush(q, (child[0] + state.value(child), (path, child)))
print(ucs(graph, startnode, endnode))
outputFile=open(outputFilename,'w')
outputFile.write(s[0])
outputFile.close()
