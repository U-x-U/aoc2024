import sys; sys.dont_write_bytecode = True; from utils import *
"""
To do: ensure Code Runner works (in WSL), have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions
Strings, lists, dicts:
lmap, ints, positive_ints, floats, positive_floats, words, keyvalues

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:
Linked, UnionFind
use deque for queue: q[0], q.append and q.popleft

List/Vector operations:
GRID_DELTA, OCT_DELTA
lget, lset, fst, snd
padd, pneg, psub, pmul, pdot, pdist1, pdist2sq, pdist2

Matrices:
matmat, matvec, matexp

Previous problems:
knot

Dict things:
dict.keys()
dict.values()
dict.items()
"""
from sortedcontainers import SortedList

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    g = Grid(lines)
    INF = 1 << 62
    dp = [Grid([[INF] * len(lines[0]) for _ in range(len(lines))]) for _ in range(4)]
    dst = None

    dir2idx = {(0, 1): 0, (-1, 0): 1, (0, -1): 2, (1, 0): 3}
    rdir2idx = {(0, -1): 0, (1, 0): 1, (0, 1): 2, (-1, 0): 3}
    idx2rdir = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    q = SortedList(key=lambda x: -x[0])
    for coord in g.coords():
        if g[coord] == 'S':
            q.add((0, coord, [0, 1]))
            dp[0][coord] = 0
        elif g[coord] == 'E':
            dst = coord
    ans = None
    while q:
        cost, pos, d = q.pop()
        if dp[dir2idx[tuple(d)]][pos] < cost:
            continue
        dp[dir2idx[tuple(d)]][pos] = cost
        if pos == dst:
            if not ans:
                ans = cost
            continue
        for nd in GRID_DELTA:
            ncost = cost
            if nd != d:
                nxt = pos
                ncost += 1000
            else:
                nxt = padd(pos, nd)
                ncost += 1
            if g.in_bounds(*nxt) and g[nxt] != '#':
                if ncost <= dp[dir2idx[tuple(nd)]][nxt]:
                    q.add((ncost, nxt, nd))

    # bfs again, starting from END
    print("ans = ", ans)
    assert(not q)
    for i in range(4):
        if dp[i][dst] == ans:
            q.add((0, dst, idx2rdir[i]))
    visited = Grid([[False] * len(lines[0]) for _ in range(len(lines))])
    while q:
        cost, pos, d = q.pop()
        if cost + dp[rdir2idx[tuple(d)]][pos] == ans:
            visited[pos] = True
        else:
            continue
        for nd in GRID_DELTA:
            ncost = cost
            if nd != d:
                nxt = pos
                ncost += 1000
            else:
                nxt = padd(pos, nd)
                ncost += 1
            if g.in_bounds(*nxt) and g[nxt] != '#':
                if ncost + dp[rdir2idx[tuple(nd)]][nxt] == ans:
                    q.add((ncost, nxt, nd))
    cnt = 0
    for coord in visited.coords():
        if visited[coord]:
            cnt += 1
    print(cnt)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""",r"""
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
