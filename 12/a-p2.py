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
    seen = Grid([[False] * g.cols for _ in range(g.rows)])

    def bfs(coord):
        q = deque([coord])
        area = 0
        sides = 0
        t = g[coord]
        def has_neighbour(coord, d):
            return g.in_bounds(*padd(d, coord))
        def connected_neighbour(coord, d):
            return has_neighbour(coord, d) and g[padd(d, coord)] == g[coord]
        while q:
            cur = q.popleft()
            area += 1
            # check upside of cur
            if not connected_neighbour(cur, [-1, 0]) \
               and (not connected_neighbour(cur, [0, -1]) or connected_neighbour(padd(cur, [0, -1]), [-1, 0])): # \
                sides += 1
            # rightside
            if not connected_neighbour(cur, [0, 1]) \
               and (not connected_neighbour(cur, [-1, 0]) or connected_neighbour(padd(cur, [-1, 0]), [0, 1])): # \
                sides += 1
            # downside
            if not connected_neighbour(cur, [1, 0]) \
               and (not connected_neighbour(cur, [0, 1]) or connected_neighbour(padd(cur, [0, 1]), [1, 0])): # \
                sides += 1
            # leftside
            if not connected_neighbour(cur, [0, -1]) \
               and (not connected_neighbour(cur, [1, 0]) or connected_neighbour(padd(cur, [1, 0]), [0, -1])): # \
                sides += 1
            seen[cur] = True
            for nb in neighbours(cur, [g.rows, g.cols], GRID_DELTA):
                if g[nb] == t and not seen[nb] and nb not in q:
                    q.append(nb)
        return area * sides
    g = Grid(lines)
    ans = 0
    for coord in g.coords():
        if not seen[coord]:
            ans += bfs(coord)
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
