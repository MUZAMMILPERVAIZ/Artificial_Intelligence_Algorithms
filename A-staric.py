

import queue
# from queue import PriorityQueue
# q=queue.PriorityQueue()
import time
def build_dcit(lis):
    di  = {}
    for i in lis:
        name = i[0]
        cost = i[1]
        di[name] = cost
    return di
def cost(x):
    return x[1]
Graph={"arad":[("zernid",75),("sibiu",140),("timisoara",118)],
            "zernid":[("oradea",71)],
            "oradea":[("sibiu",151)],
            "sibiu":[("fagaras",99),("rimnicu vilcea",80)],
            "timisoara":[("lugoj",111)],
            "lugoj":[("mehadia",70)],
            "mehadia":[("dobreta",75)],
            "dobreta":[("craiova",120)],
            "craiova":[("rimnicu vilcea",146),("pitesti",138)],
            "rimnicu vilcea":[("pitesti",97),("craiova",146)],
            "pitesti":[("bucharest",101)],
            "fagaras":[("bucharest",211)],
            "bucharest":[("giurgiu",90),("urziceni",85)],
            "giurgiu":[],
            "urziceni":[("hirsova",98),("vaslui",142)],
            "hirsova":[("eforie",86)],
            "eforie":[],
            "vaslui":[("lasi",92)],
            "lasi":[("neamt",87)],
            "neamt":[]
          }

def hn(node):
    heuristics = {
        "arad": 366,
        "bucharest": 0,
        "zernid": 374,
        "oradea": 380,
        "sibiu": 253,
        "timisoara": 329,
        "lugoj": 244,
        "mehadia": 241,
        "dobreta": 242,
        "craiova": 160,
        "rimnicu vilcea": 193,
        "pitesti": 98,
        "fagaras": 178,
        "giurgiu": 77,
        "urziceni": 80,
        "hirsova": 151,
        "eforie": 161,
        "vaslui": 199,
        "lasi": 226,
        "neamt": 234
    }
    cost = heuristics[node]
    return cost

print(Graph)
visited=[]
Queue=[]
start_time= time.time()
def A_staric(visited, dic, node=tuple, goal=None, isgoalAchieved=False, Queue=None):
    visited.append(node)
    Queue.append(node)
    while Queue:

        m=Queue.pop(0)
        print("***************")
        print("CURRENT NODE: ", m)


        if m[0] not in visited:
            visited.append(m[0])

        if m[0]==goal:
            isgoalAchieved==True
            print("GOAL ACHIEVED")
            print(time.time() - start_time)
            break
        elif isgoalAchieved==False:
            neighbours=dic.get(m[0])
            for neighbour in neighbours:
                newCost=neighbour[1]+m[1]+hn(m[0])
                name=neighbour[0]
                newNode=(name,newCost)
                if newNode[0] not  in visited and newNode[0] not in build_dcit(Queue):
                    Queue.append(newNode)
                elif newNode[0] in build_dcit(Queue):
                    oldData=build_dcit(Queue)
                    oldCost=oldData[newNode[0]]
                    oldName = newNode[0]
                    oldNode = (oldName, oldCost)

                    if newNode[1] < oldNode[1]:
                        index = Queue.index(oldNode)
                        Queue[index] = newNode
                    else:
                        pass

                Queue = sorted(Queue, key=cost)
                print("FRONTIER: ", Queue)
                print("***************")
Goal='bucharest'
isgoalAchieved=False
A_staric(visited,Graph,("arad",0),Goal,isgoalAchieved,Queue)



