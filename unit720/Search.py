# File:			Search.py
# Author: 		Luke Privett
# Date: 		02/09/2016
# Course:		CMSC 471
# E-mail:		privett1@umbc.edu
# Description:  Breadth-first, Depth-first and Uniform cost search
# Run by: python Search.py <input file> <output file> <start node> <end node> <search_type>
# References:
#            https://en.wikipedia.org/wiki/Breadth-first_search
#            https://en.wikipedia.org/wiki/Depth-first_search
#            https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# --------------------------------------------------------------------------
import sys
from collections import deque
from queue import PriorityQueue


# graph is object: tracks nodes, edges, and costs, with the id being the node and edge->cost being a dict
class Graph(object):  # create graph class consisting of nodes and edges
    nodes = set()  # unique element structure
    edges = {}  # edge-cost dictionary

    def __init__(self):  # initialize data structures
        pass  # no unique initialization needed

    # graph methods
    def add(self, node_id, edge_end, cost):
        # add the element described on the line to the graph
        if node_id not in self.edges:  # if a new node
            self.edges[node_id] = {}  # add the node

        self.edges[node_id][edge_end] = int(cost)  # cast to int
        self.nodes.add(node_id)
        self.nodes.add(edge_end)

    # readFile expects lines in file to be <START END COST>
    def read_file(self, input_file):  # file input
        with open(input_file, 'r') as file:
            for line in file:
                edge = line.split()
                self.add(edge[0], edge[1], edge[2])

    def adjacent(self, current_node):  # return nodes accessible from this node
        if current_node not in self.nodes:
            raise KeyError("Unknown Node referenced")
        try:
            return self.edges[current_node]
        except KeyError:
            return {}
# end graph


# global functions
def search(graph, search_type, start, goal):
    if search_type == "BFS":
        return bfs(graph, start, goal)
    elif search_type == "DFS":
        return dfs(graph, start, goal)
    elif search_type == "UCS":
        return ucs(graph, start, goal)
    else:
        return 'Incorrect search type'


def bfs(graph, start, goal):  # breadth-first-search (Graph, root)
    bfs_queue = deque()  # create empty queue
    visited = set()
    distance = {}  # distances from root
    parent = dict()
    current_node = ''

    # initialize search structures and verify root
    for node in graph.nodes:  # for each node in Graph
        if node == start:  # if it is the root
            distance[node] = 0  # the distance is 0
            bfs_queue.append(node)  # add root to queue
        else:
            distance[node] = float('inf')
            parent[node] = None

    while len(bfs_queue) > 0 and current_node != goal:
        current_node = bfs_queue.popleft()  # get first in queue

        if current_node in visited:
            continue  # already checked it

        for adjacent_node in graph.adjacent(current_node):  # check edges of node
            if adjacent_node not in visited and adjacent_node not in bfs_queue:  # if new node
                parent[adjacent_node] = current_node  # n.parent = current
                bfs_queue.append(adjacent_node)  # Q.enqueue(n)
        visited.add(current_node)
    # traceback
    path = []  # path as list
    if goal in parent:
        path.append(goal)
        current_node = goal
        while current_node != start:
            current_node = parent[current_node]
            path.append(current_node)
    path.reverse()
    output = ""
    for element in path:
        output += element + '\n'
    return output


def dfs(graph, start, goal):
    dfs_stack = []  # stack of nodes to check
    visited = set()  # track nodes visited
    parent = {}  # parent dictionary
    current_node = ''
    dfs_stack.append(start)

    while len(dfs_stack) > 0 and current_node != goal:
        current_node = dfs_stack.pop()  # get top node
        got_heem = False  # sentinel, must flip or node is dropped
        for adjacent in graph.adjacent(current_node):  # find adjacent nodes from current
            if adjacent not in visited:
                parent[adjacent] = current_node
                dfs_stack.append(adjacent)
                got_heem = True  # HAH!
        if not got_heem:
            dfs_stack.pop()  # abort search, the trail went cold
        visited.add(current_node)
    # traceback
    path = []
    if goal in parent:
        path.append(goal)
        current_node = goal
        while current_node != start:
            current_node = parent[current_node]
            path.append(current_node)
    path.reverse()
    output = ""
    for element in path:
        output += element + '\n'
    return output


def ucs(graph, start, goal):  # uniform cost search
    # ucs_heap = []
    ucs_queue = PriorityQueue()  # order maintaining queue
    visited = set()  # set of nodes visited
    parent = {}  # dictionary of parents from nodes
    start_tuple = 0, start
    ucs_queue.put(start_tuple)  # inserting ito priority queue as (cost_to, node)
    current_node = start
    cost_to = {start: 0}  # dict: from node, cost to get there
    queued = set()
    del start_tuple
    while not ucs_queue.empty() and current_node != goal:  # while not empty/complete
        # cost sort is hard, switching to priority queue
        # sorted_heap = sorted(ucs_queue, key=lambda cost: cost_to[cost])  # sort by cost
        # current_node = sorted_heap[0]  # current becomes lowest

        current = ucs_queue.get()  # load (cost, node) from queue
        current_node = current[1]
        # print(current_node)
        for adjacent_node in graph.adjacent(current_node):  # from adjacent nodes
            if adjacent_node not in visited:  # if not visited
                node_cost = cost_to[current_node] + graph.edges[current_node][adjacent_node]
                if adjacent_node not in cost_to or node_cost < cost_to[adjacent_node]:
                    cost_to[adjacent_node] = node_cost
                    parent[adjacent_node] = current_node
                if adjacent_node not in queued:  # put in heap if not
                    new_tuple = node_cost, adjacent_node  # sometimes you gotta take the tuple
                    ucs_queue.put(new_tuple)
                    queued.add(adjacent_node)
                    del new_tuple

        visited.add(current_node)  # list the current node as visited
    # traceback
    path = []
    if goal in parent:
        path.append(goal)
        current_node = goal
        while current_node != start:
            current_node = parent[current_node]
            path.append(current_node)
    path.reverse()
    output = ""
    for element in path:
        output += element + '\n'
    return output


def write_file(output_file, output):  # file output
    with open(output_file, 'w') as file:  # create file
        file.write(output)  # write results


def main():
    graph = Graph()  # create graph object
    # must call read_file or create elements
    graph.read_file(sys.argv[1])  # read from inputFile param
    output = str()  # create output string
    output += search(graph, sys.argv[5], sys.argv[3], sys.argv[4])
    # search(graph, type, start, end): returns output string from relevant search

    write_file(sys.argv[2], output)  # write to output file

if __name__ == "__main__":
    main()
