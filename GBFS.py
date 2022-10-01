Graph = {"arad": ["zernid", "sibiu", "timisoara"],
            "zernid": ["oradea"],
            "oradea": ["sibiu"],
            "sibiu": ["fagaras", "rimnicu vilcea"],
            "timisoara": ["lugoj"],
            "lugoj": ["mehadia"],
            "mehadia": ["dobreta"],
            "dobreta": ["craiova"],
            "craiova": ["rimnicu vilcea", "pitesti"],
            "rimnicu vilcea": ["pitesti", "craiova"],
            "pitesti": ["bucharest"],
            "fagaras": ["bucharest"],
            "bucharest": ["giurgiu", "urziceni"],
            "giurgiu": [],
            "urziceni": ["hirsova", "vaslui"],
            "hirsova": ["eforie"],
            "eforie": [],
            "vaslui": ["lasi"],
            "lasi": ["neamt"],
            "neamt": []
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


def cost(x):
    return x[1]


def built_dict(list):
    dict = {}
    for i in list:
        name = i[0]
        cost = i[1]
        dict[name] = cost
    return dict


def GBFS(start, goal):
    Queue = []
    start_val = hn(start)
    Queue.append((start, start_val))
    explored = []
    expanded = []
    while Queue:
        node = Queue.pop(0)
        print("***************")
        print("CURRENT NODE: ", node)
        if node[0] not in explored:
            explored.append(node[0])
        if node[0] == goal:
            print("GOAL ACHIEBVED")
            print("VISITED LIST:", explored)
            break
        neighbours = Graph.get(node[0])
        for neighbour in neighbours:
            new_val = hn(neighbour)
            new_node = neighbour, new_val
            if new_node[0] not in explored and new_node[0] not in built_dict(Queue):
                Queue.append(new_node)
        expanded.append(neighbour)
        Queue = sorted(Queue, key=cost)

        print("FRONTIER: ", Queue)
        print("***************")


GBFS("arad", "bucharest")