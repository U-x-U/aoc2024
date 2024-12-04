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

    ans = 0
    add_elements = lambda l1, l2: [x + y for x, y in zip(l1, l2)]
    mul_const = lambda l, c: [x * c for x in l]
    for pos in g.coords():
        if g[pos] != 'A' or not all([g.in_bounds(*add_elements(pos, d)) for d in [[-1, -1], [1, 1]]]):
            continue

        if (g[add_elements(pos, [-1, -1])] == 'M' and g[add_elements(pos, [1, 1])] == 'S' \
          or g[add_elements(pos, [-1, -1])] == 'S' and g[add_elements(pos, [1, 1])] == 'M') and \
          (g[add_elements(pos, [-1, 1])] == 'M' and g[add_elements(pos, [1, -1])] == 'S' \
          or g[add_elements(pos, [-1, 1])] == 'S' and g[add_elements(pos, [1, -1])] == 'M'):
            ans += 1
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""], do_case)
