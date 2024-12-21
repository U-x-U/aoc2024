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
    numeric = [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1'], ['A', '0']]
    direct = [['A', '^'], ['>', 'v', '<']]
    INFINITY = sys.maxsize

    def getpos(ch, g):
        for i in range(len(g)):
            for j in range(len(g[i])):
                if ch == g[i][j]:
                    return [i, j]
        return None

    @functools.cache
    def dfs(target, level) -> int:
        g = numeric if level == 0 else direct
        cur = [3, 0] if level == 0 else [0, 0]
        # cur -> getpos(target[i])
        ans = 0
        for ch in target:
            l = INFINITY
            nxt = getpos(ch, g)
            d = psub(nxt, cur)
            ntargets = []
            # 1. cur -> nxt[0], cur[1] -> nxt[0], nxt[1]
            if cur[1] < len(g[nxt[0]]):
                nt = []
                if d[0] != 0:
                    nt += ['v' if d[0] > 0 else '^' for _ in range(abs(d[0]))]
                if d[1] != 0:
                    nt += ['<' if d[1] > 0 else '>' for _ in range(abs(d[1]))]
                if nt:
                    ntargets.append(nt + ['A'])
            # 2. cur -> cur[0], nxt[1] -> nxt[0], nxt[1]
            if nxt[1] < len(g[cur[0]]):
                nt = []
                if d[1] != 0:
                    nt += ['<' if d[1] > 0 else '>' for _ in range(abs(d[1]))]
                if d[0] != 0:
                    nt += ['v' if d[0] > 0 else '^' for _ in range(abs(d[0]))]
                if nt and (not ntargets or nt != ntargets[-1]):
                    ntargets.append(nt + ['A'])

            if not ntargets:
                ntargets.append(['A'])
            for ntarget in ntargets:
                if level == 25:
                    l = min(l, len(ntarget))
                else:
                    l = min(l, dfs(''.join(ntarget), level + 1))
            cur = nxt
            ans += l
        return ans

    ans = 0
    for line in lines:
        ans += ints(line)[0] * dfs(line, 0)
    print(ans)

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
#
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

run_samples_and_actual([
# Part 1
r"""
029A
980A
179A
456A
379A
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
