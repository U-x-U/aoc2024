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
    dp = Grid([[INF] * len(lines[0]) for _ in range(len(lines))])
    dst = None

    q = SortedList(key=lambda x: -x[0])
    for coord in g.coords():
        if g[coord] == 'S':
            q.add((0, coord, [0, 1]))
            dp[coord] = 0
        elif g[coord] == 'E':
            dst = coord
    while q:
        cost, pos, d = q.pop()
        if pos == dst:
            print(cost)
            break
        if dp[pos] + 1000 < cost:
            continue
        dp[pos] = cost
        for nd in GRID_DELTA:
            nxt = padd(pos, nd)
            if g.in_bounds(*nxt) and g[nxt] != '#':
                ncost = cost + 1
                if nd != d:
                    ncost += 1000
                if ncost <= dp[nxt] + 1000:
                    q.add((ncost, nxt, nd))
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
