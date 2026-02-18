from collections import deque
def water_jug():
    start = (0, 0)
    goal = 2
    visited = set()
    q = deque([(start, [start])])
    while q:
        (x, y), path = q.popleft()
    # Check goal
        if x == goal or y == goal:
            print("Goal reached:", (x, y))
            print("Action sequence (states):")
            for step in path:
                print(step)
            return
        if (x, y) in visited:
            continue
        visited.add((x, y))
    # Generate possible moves
        actions = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x-min(x, 3-y), y + min(x, 3-y)),
            (x+min(y, 4-x), y-min(y, 4-x))
        ]
    # Add new states to queue with updated path
        for a in actions:
            if a not in visited:
                q.append((a, path + [a]))
water_jug()
