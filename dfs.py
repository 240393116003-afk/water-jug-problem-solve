visited = set()

def dfs(j1, j2, target, x=0, y=0):
    if (x, y) in visited:
        return

    print(x, y)
    visited.add((x, y))

    if x == target or y == target:
        print("Target Reached!")
        return

    dfs(j1, j2, target, j1, y)
    dfs(j1, j2, target, x, j2)
    dfs(j1, j2, target, 0, y)
    dfs(j1, j2, target, x, 0)