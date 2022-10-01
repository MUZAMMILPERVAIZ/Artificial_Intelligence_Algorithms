import time

visited=[]
Queue=[]
start_time= time.time()
def BFS(visited,dic,node,goal,isgoalAchieved=False):
    visited.append(node)
    Queue.append(node)
    while Queue:
        m=Queue.pop(0)
        print(m,end=" ")
        if m==goal:
            isgoalAchieved==True
            print("GOAL ACHIEVED")
            print(time.time() - start_time)
            break
        elif isgoalAchieved==False:
            for neighbours in dic[m]:
                if neighbours not in visited:
                    visited.append(neighbours)
                    Queue.append(neighbours)
Goal='bucharest'
isgoalAchieved=False
Frontier={"arad":["zernid","sibiu","timisoara"],
            "zernid":["arad","oradea"],
            "oradea":["zernid","sibiu"],
            "sibiu":["arad","oradea","fagaras","rimnicu vilcea"],
            "timisoara":["arad","lugoj"],
            "lugoj":["timisoara","mehadia"],
            "mehadia":["lugoj","dobreta"],
            "dobreta":["mehadia","craiova"],
            "craiova":["dobreta","rimnicu vilcea","pitesti"],
            "rimnicu vilcea":["sibiu","pitesti","craiova"],
            "pitesti":["rimnicu vilcea","craiova","bucharest"],
            "fagaras":["sibiu","bucharest"],
            "bucharest":["fagaras","pitesti","giurgiu","urziceni"],
            "giurgiu":["bucharest"],
            "urziceni":["bucharest","hirsova","vaslui"],
            "hirsova":["urziceni","eforie"],
            "eforie":["hirsova"],
            "vaslui":["lasi","urziceni"],
            "lasi":["vaslui","neamt"],
            "neamt":["lasi"]}
BFS(visited,Frontier,'arad',Goal,isgoalAchieved)
print(time.time() - start_time)