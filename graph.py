from edge import Edge
from timestamps import Timestamp
from queue import Queue
from collections import defaultdict
from collections import deque
import sys
# Global variable equivalent to infinity:
INT_MAX = sys.maxsize


class Graph(Timestamp):

    stamps = Timestamp()
    def __init__(self, N):
        self.size = N
        self.distance:list = [0] * self.size
        self.parents:list =[0] * self.size
        self.colors:list = [0] * self.size
        # self.stamps:Timestamp = []
        self.stamplist:list = [Graph.stamps]*self.size #= list()

        self.Adj = defaultdict(list)

    def addEdge(self, u:int, v:int) -> None:
        '''
        > Add an edge to our Graph G from U->V
        '''
        self.Adj[u].append( Edge(v,0) )

    #end-AddEdge

    def BFS(self, s) -> None:
        for i in range(self.size):
            self.distance[i] = INT_MAX
            self.parents[i] = i
        
        self.distance[ s ] = 0
        aQ = Queue()
        aQ.put( s )
        
        while( aQ.empty() == False ):
            u = aQ.get()
            # print("U", u)
            
            for i in range(len(self.Adj[ u ])):
                v = self.Adj[u][i].neighbor
                # print("(u,v) \t",u, "->", v)
                if self.distance[v] == INT_MAX:
                    # set distance, parents and push into queue
                    self.distance[v] = self.distance[u] + 1
                    self.parents[v] = u
                    aQ.put( v )
                #end-if(reachable)
            #end-for (edge)
        #end-while(items in Q)
    #end-BFS


    def printParents(self) -> None:
        # for i in range(self.size):
        print('Parents: ')
        print(type(self.parents))
        print(len(self.parents))
        for v in range(len(self.parents)):
            print(self.parents[v])
        #end-for
    #end-printParents


    def printDistance(self) -> None:
        print('Distance: ')
        for v in range(len(self.distance)):
            print(self.distance[v])
        #end-for
    #end-printDistance

    def printColors(self) -> None:
        print('Colors: ')
        for v in range(len(self.colors)):
            print(self.colors[v])
        #end-for
    #end-printColors
    def printStamps(self) -> None:
        print('TimeStamps: ')
        for v in range(len(self.stamplist)):
            print(self.stamplist[v].disc, self.stamplist[v].final)
        #end-for
    #end-print-timeStamps

    def bfsPrint(self, s):
        pass

    def printGraph(self):
        for u in range(self.size):
            # print()
            for i in range(len( self.Adj[u] )):
                v = self.Adj[u][i].neighbor
                # print
                print(u, v)
            # print(v, '\n')
    #end-print_graph

    def printPath(self, s, r):
        '''
        > Recursive algorithm to 'backtrack' shortest path given by BFS algorithm and parents(ancestors) array
            > s is the source
            > r is the target Vertex
        '''
        print('PrintPath...')
        if r == self.parents[r]: # we've made it back to the source
            print(r)
            return
        self.printPath(s, self.parents[r] )
        print(r)
    #end-printPath

    def DFS(self) -> None:
        '''
        > Depth First Search algorithm used to traverse a graph G and visit each vertex V
        '''
        for i in range(self.size):
            self.parents[i] = i
            self.colors[i] = 'W'
        
        t = 0

        for i in range(self.size):
            if self.colors[i] == 'W':

                self.DFS_Visit( i, t)
            # end-if
        #end-for
    #end-DFS

    def DFS_Visit(self, u, t):

        self.colors[u] = 'G'
        self.stamplist[u].disc = t
        # self.stamps[u] = t
        t = t+1

        for i in range(len(self.Adj[u])):
            v = self.Adj[u][i].neighbor  # get U's neighbor
            if self.colors[v] == 'W': # we still need to visit the Node
                # Mark the Node information as we visit 
                self.parents[v] = u 
                self.distance[v] = self.distance[u] + 1
                self.colors[v] = 'G' # Mark the Node as visited. Could also use a boolean value here called 'found' to mark each Node.found=True
                self.DFS_Visit(v, t)
            # end-if
        # end-for

        # if it makes it any further set the finishing time of the node and set color to 'Black'
        self.colors[u] = 'B'
        self.stamplist[u].final = t 
        # self.stamps[u] = t 
        t = t+1
    #end-DFS_Visit
    

