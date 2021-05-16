from os import linesep
import sys
from edge import Edge
from graph import Graph
# adj = list(list())

adj = [ [2,1],\
    [0,3],\
        [0,3,4,5,6],\
            [1,2,5],\
                [2,5,6],\
                    [2,3,4,6],\
                        [2,4,5]\
                        ]
# print('Length: ')
# print(len(adj))
# vs = list()
# uv =  dict()
# # uv.get
# for u in range(0,(len(adj))):
#     print("U->",u)
#     for i in range(len(adj[u])):
#         v = adj[u][i]
#         print(u,"->", v)
 
# def printPath(aGraph:Graph, s, r):
#     print('PrintPath...')
#     if aGraph.parents[r] != r:
#         return 
#     else:
#         printPath(Graph, s, aGraph.parents[r])
#         print(r)

def printPath(parents, r):
    print('PrintPath...')
    if parents[r] == r:
        print(r)
        print("yes")
        return 
    else:
        printPath(parents, parents[r])
        print(r)
        

if __name__ == "__main__":
    agraph = Graph(13)
    agraph.addEdge(0, 2)
    # agraph.addEdge(0, 1)
    agraph.addEdge(0, 3)
    agraph.addEdge(1,3)
    agraph.addEdge(2,3)
    agraph.addEdge(2,4)
    agraph.addEdge(2,5)
    agraph.addEdge(2,6)
    agraph.addEdge(3,5)
    agraph.addEdge(5,4)
    agraph.addEdge(4,6)
    agraph.addEdge(5,6)
    agraph.addEdge(3,4)

    # lines = ['addEdge 0 2', 'addEdge 0 3']
    # for line in lines:
    #     if 'addEdge' in line.split():
    #         print(type(line))
    #         print(line.split())
    #         cmd = line.split()[0]
    #         u = line.split()[1]
    #         v = line.split()[2]
    #         print(cmd, u, v)

            # for cmd in line:
            #     print(cmd)


    # agraph.BFS(0)
    # parents = agraph.parents
    with open(sys.argv[1], 'r') as f:
        print(sys.argv[1])
        # contents = f.read()
        lines = f.readlines()
        print("Type: ", type(lines))
        print("length: ", len(lines))
        # print("Lines:")
        # print(lines)
        for line in lines:
            commands = line.split()

            if 'size' in commands:
                size = int(commands[1])
                graph = Graph( size )

            elif 'addEdge' in commands:
                u = int(commands[1])
                v = int(commands[2])
                graph.addEdge(u, v)
                print('Added Edge')
                print("(u,v) \t", u, '->', v)

            elif 'BFS' in commands:
                # print("BFS:")
                s = int(commands[1])
                print("Run Bfs on Source:", s)
                graph.BFS( s )
                graph.printParents()
                graph.printDistance()
            elif 'DFS' in commands:
                graph.DFS()
                graph.printParents()
                graph.printColors()
                graph.printStamps()

            elif 'printGraph' in commands:
                graph.printGraph()

            else:
                print('ERROR:\t command {} not found'.format(line))



        # for cmd in lines:
        #     # print("CMD>> " , cmd)
        #     if cmd == 'addEdge':
        #         print(cmd)
        #     elif cmd == 'BFS':
        #         source = input("Enter integer source you would like to run BFS: \t")
        #         source = int(source)
        #         agraph.BFS(source)
        #     else:
        #         print('Command {} not found'.format(cmd))
        # cmd = sys.argv[1]
        # print(lines)
        # for cmd in contents:
            # print(cmd)
    # print("Content: " , contents)

    # agraph.printGraph()
    # printPath(agraph, 0 , 6)
    # printPath(parents=parents, r=4)
    # agraph.printPath(0, 5)
