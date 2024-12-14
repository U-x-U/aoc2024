import sys; sys.dont_write_bytecode = True; from utils import *
from math import gcd
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
    lines = deque(inp.splitlines())

    ans = 0
    while lines:
        ax, ay =  tuple(ints(lines.popleft()))
        bx, by =  tuple(ints(lines.popleft()))
        x, y =  tuple(lmap(lambda x: x + 10_000_000_000_000, ints(lines.popleft())))
        # ay * ax * i + ay * bx * j = ay * x
        # ax * ay * i + ax * by * j = ax * y
        # (ay * bx - ax * by) * j = ay * x - ax * y

        if ay * bx == ax * by:
            print("xxxxxxxxxxxxxxxxxxxx")
        elif (ay * x - ax * y) % (ay * bx - ax * by) == 0:
            j = (ay * x - ax * y) // (ay * bx - ax * by)
            if (x - bx * j) % ax == 0:
                i = (x - bx * j) // ax
                if i >= 0 and j >= 0:
                    ans += 3 * i + j
        if lines:
            lines.popleft()
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
