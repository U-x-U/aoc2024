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
def paddmod(x, y, z):
    return [(a + b) % c for a, b, c in zip(x, y, z)]

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    dim = [11, 7] if sample else [101, 103]
    robots = []
    for line in inp.splitlines():
        p, v = map(ints, line.split(' '))
        robots.append((p, v))
    ul, ur, dl, dr = 0, 0, 0, 0
    for i in range(len(robots)):
        pos = paddmod(robots[i][0], pmul(100, robots[i][1]), dim)
        if pos[0] < dim[0] // 2 and pos[1] < dim[1] // 2:
            ul += 1
        elif pos[0] < dim[0] // 2  and pos[1] > dim[1] // 2:
            dl += 1
        elif pos[0] > dim[0] // 2 and pos[1] < dim[1] // 2:
            ur += 1
        elif pos[0] > dim[0] // 2 and pos[1] > dim[1] // 2:
            dr += 1
    print(ul * ur * dl * dr)

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
