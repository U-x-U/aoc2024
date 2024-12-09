import sys; sys.dont_write_bytecode = True; from utils import *
from sortedcontainers import SortedList
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
    digits = [int(d) for d in inp]
    files = {}
    free = SortedList()

    st = 0
    for (i, d) in enumerate(digits):
        ed = st + d
        if i % 2 == 0:
            files[i // 2] = (st, ed)
        elif d != 0:
            free.add((st, ed))
        st = ed


    # check all files in id dec order
    for i in range(len(files) - 1, -1, -1):
        (fst, fed) = files[i]
        fsz = fed - fst
        for (st, ed) in free:
            # always move to the left
            if st >= fed:
                break
            sz = ed - st
            if sz >= fsz:
                free.remove((st, ed))
                if sz > fsz:
                    free.add((st + fsz, ed))
                files[i] = (st, st + fsz)
                free.add((fst, fed))
                break
    ans = 0
    for i in files:
        (st, ed) = files[i]
        ans += i * (ed - 1 + st) * (ed - st) // 2
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
2333133121414131402
""", r"""
12345
"""], do_case)
