import heapq
goal = (1,2,3,4,5,6,7,8,0)
def manhattan(state):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            dist += abs(i//3-goal_pos//3) + abs(i%3-goal_pos%3)
    return dist
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    moves = {-3, 3,-1, 1 }
    for m in moves:
        new = idx + m
        if 0 <= new < 9:
            new_state = list(state)
            new_state[idx], new_state[new] = new_state[new], new_state[idx]
            print(new_state)
            neighbors.append(tuple(new_state))
    return neighbors
def astar(start):
    pq = [(manhattan(start), 0, start)]
    visited = set()
    while pq:
        f, g, state = heapq.heappop(pq)
        if state == goal:
            print("Solved!")
            return
        if state in visited:
            continue
        visited.add(state)
        for n in get_neighbors(state):
            heapq.heappush(pq, (g + 1 + manhattan(n), g + 1, n))
start = (1,2,3,4,0,5,6,7,8)
astar(start)
