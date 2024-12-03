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
from itertools import dropwhile

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    lines = map(ints, lines)
    diffs = list(map(list_diff, lines))

    inrange = lambda x: 1 <= abs(x) and abs(x) <= 3
    is_safe = lambda l: inrange(l[0]) and all(signum(x) == signum(y) and inrange(y) for x, y in zip(l[:], l[1:]))

    ans = sum(map(lambda diff:
                  is_safe(diff[1:])
                  or is_safe(diff[:-1])
                  or any(map(lambda i:
                             is_safe(diff[: i-1] + [diff[i-1] + diff[i]] + diff[i+1:]), range(1, len(diff)))),
                  diffs))
    print(ans)

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""], do_case)
