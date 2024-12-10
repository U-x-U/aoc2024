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
    start_pos = []
    for pos in g.coords():
        if g[pos] == '0':
            start_pos.append(make_hashable(pos))

    @functools.cache
    def calc_score(pos, cur) -> int:
        if cur == 9:
            return 1;
        ans = 0
        cur += 1
        for d in GRID_DELTA:
            npos = padd(pos, d)
            if g.in_bounds(*npos) and g[npos] == str(cur):
                ans += calc_score(make_hashable(npos), cur)
        return ans

    ans = 0
    for st in start_pos:
        ans += calc_score(st, 0)
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""",r"""
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
""",r"""
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
