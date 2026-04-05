from collections import deque

def bfs(j1, j2, target):
    visited = set()
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue

        print(x, y)
        visited.add((x, y))

        if x == target or y == target:
            print("Target Reached!")
            return

        q.append((j1, y))   # fill jug1
        q.append((x, j2))   # fill jug2
        q.append((0, y))    # empty jug1
        q.append((x, 0))    # empty jug2

        pour = min(x, j2 - y)
        q.append((x - pour, y + pour))

        pour = min(y, j1 - x)
        q.append((x + pour, y - pour))