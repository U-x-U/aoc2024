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

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    g = Grid(lines)

    st, ed = None, None
    for coord in g.coords():
        if g[coord] == 'S':
            st = coord
        elif g[coord] == 'E':
            ed = coord

    path = []
    while st != ed:
        path.append(st)
        for d in GRID_DELTA:
            nxt = padd(d, st)
            if g.in_bounds(*nxt) and g[nxt] != '#' and (len(path) == 1 or path[-2] != nxt):
                st = nxt
                break
    path.append(ed)

    ans = 0
    for i in range(len(path)):
        for j in range(i + 100, len(path)):
            x, y = path[i], path[j]
            shortest = sum(abs(i) for i in psub(x, y))
            if shortest > 20:
                continue
            if abs(i - j) - shortest >= 100:
                ans += 1
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
