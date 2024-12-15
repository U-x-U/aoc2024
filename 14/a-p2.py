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
    pos = []
    vel = []
    tiles = [[0] * dim[0] for _ in range(dim[1])]
    for line in inp.splitlines():
        p, v = map(ints, line.split(' '))
        pos.append(p)
        vel.append(v)
        tiles[p[1]][p[0]] += 1

    def connectivity(pos, tiles) -> float:
        cnt = 0
        for p in pos:
            j, i = tuple(p)
            if i >= 1 and tiles[i - 1][j]\
               or i < dim[1] - 1 and tiles[i + 1][j]\
               or j >= 1 and tiles[i][j - 1]\
               or j < dim[0] - 1 and tiles[i][j + 1]:
                cnt += 1
        return cnt / len(pos)

    for t in range(10000):
        for i in range(len(pos)):
            tiles[pos[i][1]][pos[i][0]] -= 1
            pos[i] = paddmod(pos[i], vel[i], dim)
            tiles[pos[i][1]][pos[i][0]] += 1
        if connectivity(pos, tiles) > 0.7:
            print("time = ", t + 1)
            for x in range(dim[1]):
                for y in range(dim[0]):
                    print('.' if tiles[x][y] != 0 else ' ', end='')
                print()

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



actual_input = get_actual().strip("\n")
do_case(actual_input, False)
# run_samples_and_actual([
# # Part 1
# r"""
# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# """,r"""

# """,r"""

# """,r"""

# """,r"""

# """,r"""

# """,r"""

# """], do_case)
