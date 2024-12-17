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
from itertools import takewhile

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = iter(inp.splitlines())
    regs = flatten(lmap(ints, takewhile(lambda x: x, lines)))
    programs = ints(next(lines))
    print(regs, programs)

    ip = 0
    def combo(op):
        if op <= 3:
            return op
        if op <= 6:
            return regs[op - 4]

    ans = ''
    while True:
        if ip + 1 >= len(programs):
            break
        op = programs[ip + 1]
        match programs[ip]:
            case 0:
                regs[0] //= 1 << combo(op)
            case 1:
                regs[1] ^= op
            case 2:
                regs[1] = combo(op) % 8
            case 3:
                if regs[0] != 0:
                    ip = op - 2
            case 4:
                regs[1] = regs[1] ^ regs[2]
            case 5:
                ans += str(combo(op) % 8) + ','
            case 6:
                regs[1] = regs[0] // (1 << combo(op))
            case 7:
                regs[2] = regs[0] // (1 << combo(op))
        ip += 2
    print(ans[:-1])

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
