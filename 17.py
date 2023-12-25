from queue import PriorityQueue # essentially a binary heap

def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: (0, 0, 'O', float('inf'))} # (x, y, z, x1): x - distance, y - number of z moves, z - move, x1 - distance but second shortest
    parent = {start: None}
    todo = PriorityQueue()
  
    todo.put((0, float('inf'), start))
    while todo:
        while not todo.empty():
            _, _, vertex = todo.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else: # if todo ran out
            break # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue # skip these to save time
            old_cost_tuple = cost.get(neighbor, (float('inf'), float('inf'), 'X', float('inf'))) # default to infinity
            old_cost = old_cost_tuple[0]
            old_cost_2 = old_cost_tuple[3]
            new_cost = cost[vertex][0] + distance[0]
            new_cost_tuple = (new_cost, 1, distance[2], cost[vertex][3])
            # print('distance', distance)
            # print('cost vertex', cost[vertex])
            if distance[2] == cost[vertex][2]:
                # print('equal')
                if cost[vertex][1] >= 3:
                    new_cost = cost[vertex][3] + distance[0]
                    new_cost_tuple = (new_cost, 1, distance[2], cost[vertex][3])
                else:
                    new_cost_tuple = (new_cost, cost[vertex][1]+1, distance[2], cost[vertex][3])
            if new_cost < old_cost:
                new_cost_tuple = (new_cost_tuple[0], new_cost_tuple[1], new_cost_tuple[2], old_cost)
                todo.put((new_cost, old_cost, neighbor))
                cost[neighbor] = new_cost_tuple
                parent[neighbor] = vertex
                print('set distance from', start, 'to', neighbor, ':', new_cost_tuple)
            elif new_cost < old_cost_2:
                new_cost_tuple = (old_cost_tuple[0], old_cost_tuple[1], old_cost_tuple[2], new_cost)
                # todo.put((old_cost, new_cost, neighbor))
                todo.put((new_cost, old_cost_tuple[0], neighbor))
                print('set second shortest distance from', start, 'to', neighbor, ':', new_cost, 'from', old_cost_2)
                cost[neighbor] = new_cost_tuple

    return parent

def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None: # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


## Example

G = { # random example graph
 'A': {('C', 76)},
 'B': {('C', 20), ('J', 78)},
 'C': {('C', 62), ('F', 99), ('G', 72), ('H', 40)},
 'D': {('A',  8), ('G', 71), ('I', 61)},
 'E': {('C', 16), ('E', 54), ('I',  3)},
 'F': {('J', 66)},
 'G': {('B', 92), ('E', 48), ('G', 31)},
 'H': {('G', 36)},
 'I': {('J', 88), ('K', 16)},
 'J': {('H',  4), ('K', 46)},
 'K': {('I', 40)}
}

# parent = dijkstra(G, 'A', 'K')
# print(make_path(parent, 'K'))

# -> ['A', 'C', 'G', 'E', 'I', 'K']

lines = list(open('17.txt', 'r'))
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        from1 = (i, j)
        G[from1] = {(from1, 0)}
        if j > 0:
            to1 = (i, j-1)
            w1 = (int(lines[i][j-1]), 1, 'L')
            G[from1].add((to1, w1))
        if i > 0:
            to1 = (i-1, j)
            w1 = (int(lines[i-1][j]), 1, 'U')
            G[from1].add((to1, w1))
        if j < m-1:
            to1 = (i, j+1)
            w1 = (int(lines[i][j+1]), 1, 'R')
            G[from1].add((to1, w1))
        if i < n-1:
            to1 = (i+1, j)
            w1 = (int(lines[i+1][j]), 1, 'D')
            G[from1].add((to1, w1))

parent = dijkstra(G, (0, 0), (n-1, m-1))
path = make_path(parent, (n-1, m-1))
ans = 0
for p in path:
    if (p[0], p[1]) == (0, 0):
        continue
    print(p[0], p[1], lines[p[0]][p[1]])
    ans += int(lines[p[0]][p[1]])
print(ans)