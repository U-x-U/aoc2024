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
    lines = iter(inp.splitlines())
    locks = []
    keys = []
    sz = 5
    while True:
        cur = list(itertools.takewhile(lambda x: x, lines))
        if not cur:
            break
        if cur[0][0] == '#':
            lock = []
            for c in range(len(cur[0])):
                cnt = 0
                for r in range(1, len(cur)):
                    if cur[r][c] == '#':
                        cnt += 1
                    else:
                        break
                lock.append(cnt)
            locks.append(lock)
        else:
            key = []
            for c in range(len(cur[0])):
                cnt = 0
                for r in reversed(range(len(cur) - 1)):
                    if cur[r][c] == '#':
                        cnt += 1
                    else:
                        break
                key.append(cnt)
            keys.append(key)
    ans = 0
    for lock in locks:
        for key in keys:
            if all(map(lambda p: p[0] + p[1] <= sz, zip(lock, key))):
                ans += 1
    print(ans)


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
