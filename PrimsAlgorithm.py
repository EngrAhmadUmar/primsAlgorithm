#Prim's Algorithm

#Creating our adjacency matrix representing edges and vertices of the graph
graph = [[0,28,0,0,0,10,0],
    [28,0,16,0,0,0,14],
    [0,16,0,12,0,0,0],
    [0,0,12,0,22,0,18],
    [0,0,0,22,0,25,24],
    [10,0,0,0,25,0,0],
    [0,14,0,18,24,0,0]]
    
#Specifying our number of vertices in the graph.
v = 7
    

#Create an array to help check visited edges vertex
visited = [0] * v

#Initializing the number of edge
no_edge = 0

#Setting our zero index value to be True
visited[0] = True

while (no_edge < v - 1):
    #Initializing our variables
    minimum = float("inf")
    x = 0
    y = 0
    #Running a looping through every vertex in the graph
    for i in range(v):
        if visited[i]:
            #Looping through all the adjacent vertices connected to our selected vertex above
            for j in range(v):
                if ((not visited[j]) and graph[i][j]):  
                    #Not in selected and there is an edge
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(str(x+1) + "-->" + str(y+1) + ":" + str(graph[x][y]))
    #Here we set the visited vertex to true
    visited[y] = True
    #Lastly we increment the number of edges
    no_edge += 1
