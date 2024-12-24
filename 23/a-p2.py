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
    g = dict()
    st = set()
    for line in lines:
        a, b = line.split('-')
        if a not in g:
            g.setdefault(a, set())
        if b not in g:
            g.setdefault(b, set())
        g[a].add(b)
        g[b].add(a)
        st.add(a)
        st.add(b)

    def findmax(st, g):
        if len(st) == 2:
            for x in st:
                if len(g[x]) != 0:
                    return list(st)
            return list(st)[:1]
        if len(st) == 1:
            return list(st)
        group = []
        for x in st:
            for y in g:
                if x in g[y]:
                    g[y].remove(x)
            # find the max group that has x
            g1 = dict(g)
            for y in st - g[x]:
                if y in g1:
                    g1.pop(y)
            for y in g1:
                g1[y] &= g[x]
            mx = findmax(g[x], g1)
            if 1 + len(mx) > len(group):
                group = [x] + mx
            g.pop(x)
        return group
    mxgroup = findmax(st, g)
    print(','.join(sorted(mxgroup)))
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)