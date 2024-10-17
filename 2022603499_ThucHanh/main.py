# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
graph = {
    'A': {'B': 20, 'C': 15, 'E': 80},
    'B': {'A':40, 'E': 10, 'F':30},
    'C': {'A':20, 'B':4, 'F':10},
    'D': {'A':36 ,'B': 18, 'C':15},
    'E': {'C':90, 'D':15},
    'F': {'C':45, 'E':10}
}

graph2 = {
    'A' : {'F':2, 'B':1, 'G':4},
    'B' : {},
    'C' : {'A' : 1},
    'D' : {'F' : 1},
    'E' : {'D' : 2},
    'F' : {'E' : 2},
    'G' : {'C' : 1, 'E' : 1, 'J' :1},
    'H' : {'G' : 3, 'I' : 1},
    'I' : {'H' : 1},
    'J' : {'K': 1, 'M':2, 'L':3},
    'L' : {'G': 2, 'M':1},
    'M' : {'L' : 1},
    'K' : {}
}

def cost_and_path (start, goal, parent, g):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print("Duong di: {}".format(path))
    print("Chi phi: {}".format(g[goal]))

def AT(graph , start, goals):
    MO = [start]
    DONG = []
    g = {start: 0}
    parent = {}
    while MO:
        min = float('inf')
        n = None
        for i in MO:
            if i in g:
                cost = g[i]
            else:
                cost = float('inf')
            if cost < min:
                min = cost
                n = i
        if n in goals:
            cost_and_path(start, n, parent, g)
            return True

        MO.remove(n)
        DONG.append(n)

        for i in graph.get(n,{}):
            cost = graph[n][i]
            new_cost = g.get(n, float('inf')) + cost
            if i in parent and new_cost < g[i]:
                g[i] = new_cost
                parent[i] = n
            elif i not in MO and i not in DONG:
                g[i] = new_cost
                parent[i] = n
                MO.append(i)

    return False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if AT(graph2, 'A', 'M') == False:
        print("Khong tim thay duong di !")
