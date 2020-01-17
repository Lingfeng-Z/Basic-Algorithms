import random

class Graph():
    def __init__(self, x: list, rule: str):
        self.dim = x[0][0]
        self.name_list = [tuple(x[i][:-1]) for i in range(len(x)) if i != 0]
        self.energy_list = [x[i][-1] for i in range(len(x)) if i != 0]
        self.energy_dict = {}
        self.link_dict = {}
        self.rule = rule
        self.makeGraph()

    def makeGraph(self):
        i = 0
        while i < len(self.name_list):
            self.energy_dict[self.name_list[i]] = self.energy_list[i]
            i += 1
        i = 0
        while i < len(self.name_list):
            self.link_dict[self.name_list[i]] = self.findLinkNodes(self.name_list[i])
            i += 1
        if self.rule == "desc":
            max_value = max(self.energy_dict.values())
            self.startpoint = random.choice([x for x in self.energy_dict if self.energy_dict[x] == max_value])
        else:
            min_value = min(self.energy_dict.values())
            self.startpoint = random.choice([x for x in self.energy_dict if self.energy_dict[x] == min_value])

    def findLinkNodes(self, currentNode: list):
        Node = list(currentNode)
        linklist = []
        for i in range(3):
            for j in [-1, 1]:
                if Node[i] + j >=0 and Node[i] + j< self.dim:
                    if self.energy_dict[tuple(Node[0:i]+[Node[i] + j]+Node[i+1:])] < self.energy_dict[currentNode]:
                        linklist.append(tuple(Node[0:i]+[Node[i] + j]+Node[i+1:]))
        return linklist


class GraphSearch():
    def __init__(self, graph: Graph):
        self.stack = []
        self.visited_dict = {}
        for x in graph.link_dict:
            for y in graph.link_dict[x]:
                self.visited_dict[x,y] = False
        self.stack.append(graph.startpoint)
        self.max_energy, self.route = self.DFS(graph)

    def DFS(self, graph: Graph):
        max_energy = 0
        sum_energy = 0
        pop_out = []
        while len(self.stack) != 0:
            current_point = self.stack[-1]
            nodesLinked = graph.link_dict[current_point]
            visit_nodesLinked = [self.visited_dict[current_point,x] for x in nodesLinked]
            if False in visit_nodesLinked:
                for x in nodesLinked:
                    if self.visited_dict[current_point,x] == False:
                        self.visited_dict[current_point,x] = True
                        if len(pop_out) > 1:
                            for y in pop_out:
                                for _ in graph.link_dict[y]:
                                    self.visited_dict[y,_] = False
                        pop_out = []
                        self.stack.append(x)
                        break
            else:
                for x in self.stack:
                    sum_energy += graph.energy_dict[x]
                if sum_energy > max_energy:
                    max_energy = sum_energy
                    max_stack = self.stack
                sum_energy = 0
                pop_out.append(self.stack[-1])
                '''if len(self.stack) != 1:
                    self.visited_dict[self.stack[-2], self.stack[-1]] = True'''
                self.stack = self.stack[:-1]
        return max_energy, max_stack



if __name__ == "__main__":
    input = [[2], [0,0,0,7], [0,0,1,2], [0,1,0,4], [0,1,1,3], [1,0,0,6], [1,0,1,1], [1,1,0,5], [1,1,1,0]]
    input1 = [[3],
        [0,0,0,1],
        [0,0,1,2],
        [0,0,2,3],
        [0,1,0,4],
        [0,1,1,5],
        [0,1,2,6],
        [0,2,0,7],
        [0,2,1,8],
        [0,2,2,9],
        [1,0,0,10],
        [1,0,1,11],
        [1,0,2,12],
        [1,1,0,13],
        [1,1,1,14],
        [1,1,2,13],
        [1,2,0,12],
        [1,2,1,11],
        [1,2,2,10],
        [2,0,0,9],
        [2,0,1,8],
        [2,0,2,7],
        [2,1,0,6],
        [2,1,1,5],
        [2,1,2,4],
        [2,2,0,3],
        [2,2,1,2],
        [2,2,2,1]]
    graph1 = Graph(input1, "desc")
    Solu = GraphSearch(graph1)
    print(Solu.max_energy, Solu.route)





