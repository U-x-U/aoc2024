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
    lines = [list(line) for line in lines]
    g = Grid(lines)
    g1 = Grid(lines)
    mp = {}
    for pos in g.coords():
        if g[pos] == '.':
            continue
        if g[pos] not in mp:
            mp[g[pos]] = []
        mp[g[pos]].append(pos)
    for k in mp:
       for (x, y) in itertools.combinations(mp[k], 2):
           d = psub(y, x)
           if g.in_bounds(*padd(y, d)):
               g1[padd(y, d)] = '#'
           if g.in_bounds(*psub(x, d)):
               g1[psub(x, d)] = '#'

    print(sum(map(lambda l: l.count('#'), g1.grid)))

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""], do_case)
