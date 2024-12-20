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

    mp = {}
    for coord in g.coords():
        if g[coord] != '#':
            continue
        nbs = []
        for d in GRID_DELTA:
            nb = padd(d, coord)
            if g.in_bounds(*nb) and g[nb] != '#':
                nbs.append(nb)
        assert(len(nbs) < 4)
        for x, y in itertools.combinations(nbs, 2):
            xidx = path.index(x)
            yidx = path.index(y)
            dist = abs(yidx - xidx) - 2
            mp.setdefault(dist, 0)
            mp[dist] += 1
    ans = 0
    for k in mp:
        if k >= 100:
            ans += mp[k]
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
