"""
class Node:
    def __init__(self, state, parent, actions, cost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.cost = cost
def DFS():
initialState= 'A'
goalState = 'D'
graph = {
    'A': Node('A', None, ['B', 'E', "C"], None),
    'B': Node('B', None, ['D', 'E', "A"], None),
    'C': Node('C', None, ['A', 'F', 'G'], None),
    'D': Node('D', None, ['B', 'E'], None),
    'E': Node('E', None, ['A', 'B', 'D'], None),
    'F': Node('F', None, ['C'], None),
    'G': Node('G', None, ['C'], None), }
frontier=[initialState]
explored=[]
while len(frontier)!=0:
    currentNode=frontier.pop(len(frontier)-1)
    print(currentNode)
    explored.append(currentNode)
    currentChild= 0
    for child in graph[currentNode]:
        if child not in frontier and child not in explored:
            graph[child].parent==currentChild
            if graph[child].parent==currentChild:
                print(explored)
                return actionSequence (graph, initialState, goalState)
            currentChild=currentChild+1
            frontier.append(child)
            if currentChild==0:
               def explored [len (explored)-1]
 solution DFS()
 print(solution)
"""
#Task
#Depth-First-Search
import time
visited=[]
Stack=[]
start_time= time.time()
def DFS(visited,dic,node,goal,isgoalAchieved=False):
    visited.append(node)
    Stack.append(node)
    while Stack:
        m=Stack.pop()
        print(m, end=" ")

        if m==goal:
            isgoalAchieved==True
            print("GOAL ACHIEVED")
            print(time.time() - start_time)
            break
        elif isgoalAchieved==False:
            for neighbours in dic[m]:
                if neighbours not in visited:
                    visited.append(neighbours)
                    Stack.append(neighbours)

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
DFS(visited,Frontier,'sibiu',Goal,isgoalAchieved)
print(time.time() - start_time)