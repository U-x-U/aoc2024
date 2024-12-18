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
    sz = 7 if sample else 71
    bt = 12 if sample else 1024
    g = [['.'] * sz for _ in range(sz)]
    for line in lines[:bt]:
        y, x = tuple(ints(line))
        g[x][y] = '#'
    G = Grid(g)

    q = deque([[0, 0]])
    seen = Grid([[False] * sz for _ in range(sz)])
    ans = 0
    while q:
        ans += 1
        qlen = len(q)
        for i in range(qlen):
            pos = q.popleft()
            if seen[pos]:
                continue
            else:
                seen[pos] = True
            if pos == [sz - 1, sz - 1]:
                print(ans)
                return
            for d in GRID_DELTA:
                npos = padd(d, pos)
                if G.in_bounds(*npos) and G[pos] == '.' and not seen[npos]:
                    q.append(npos)

    print(ans)
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
