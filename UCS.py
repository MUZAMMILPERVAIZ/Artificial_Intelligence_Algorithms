

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
print(Graph)
visited=[]
Queue=[]
start_time= time.time()
def UCS(visited, dic, node=tuple, goal=None, isgoalAchieved=False, Queue=None):
    visited.append(node)
    Queue.append(node)
    while Queue:
        m=Queue.pop(0)
        print(m)

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
                newCost=neighbour[1]+m[1]
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
                print(50 * '*')
Goal='bucharest'
isgoalAchieved=False
UCS(visited,Graph,("arad",0),Goal,isgoalAchieved,Queue)



