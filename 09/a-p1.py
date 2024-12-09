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
    digits = [int(d) for d in inp]
    files = deque()
    free = []

    st = 0
    for (i, d) in enumerate(digits):
        ed = st + d
        if i % 2 == 0:
            files.appendleft((i // 2, st, ed))
        else:
            free.append((st, ed))
        st = ed

    for (st, ed) in free:
        while ed > st and files[0][1] >= ed:
            (idx, fst, fed) = files.popleft()
            if fed - fst > ed - st:
                files.appendleft((idx, fst, fed - ed + st))
            files.append((idx, st, min(ed, st + fed - fst)))
            st = min(ed, st + fed - fst)

    print(sum(map(lambda x: x[0] * (x[2] - 1 + x[1]) * (x[2] - x[1]) // 2, files)))
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
2333133121414131402
""", r"""
12345
"""], do_case)
