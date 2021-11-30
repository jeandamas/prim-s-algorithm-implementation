# This code is the implementation of prim's algorighm

INFINITY = 9999999999
# The available vertices in xgiven graph
N = 7
#creatinGraphgraph by adjacency matrix method
Graph = [[0,28,0,0,0,10,0],
        [26,0,16,0,0,0,14],
        [0,16,0,12,0,0,0],
        [0,0,12,0,22,0,25,0,18],
        [0,0,0,22,0,25,0,25,24],
        [10,0,0,0,25,0,0],
        [0,14,0,18,24,0,0]]

selected_node = [0, 0, 0, 0, 0, 0, 0]

no_of_edge = 0

selected_node[0] = True

# printinGraphfor edge and weight
graphWeight=0;
print("\n\nEdge : Weight\n")
print("------------")
while (no_of_edge < N - 1):
    
    min = INFINITY
    x= 0
    y= 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and Graph[m][n]):  
                    # avoid repeatinGraphthe same the used edge
                    if min > Graph[m][n]:
                        min = Graph[m][n]
                        x= m
                        y= n
    print(str(int(x+1)) + "---" + str(int(y+1)) + " : " + str(Graph[x][y]))
    selected_node[y] = True
    graphWeight+=int(str(Graph[x][y]))
    no_of_edge += 1
print("Cost of Minimum Spanning Tree is " + str(graphWeight)+"\n\n")
