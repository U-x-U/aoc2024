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
# import os

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    # lines = iter(inp.splitlines())
    # regs_orig = flatten(lmap(ints, takewhile(lambda x: x, lines)))
    # programs = ints(next(lines))
    programs = [2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0]

    mp = {}
    for i in range(1 << 10):
        b = (i % 8) ^ 3
        c = i // (1 << b)
        b = b ^ c ^ 5
        b %= 8
        if b not in mp:
            mp[b] = []
        mp[b].append(format(i, '010b'))

    candidates = mp[programs[0]]
    for i, out in enumerate(programs[1:]):
        # digit 3i+3 ~ 3i+10 (incl) must be among mp[out]
        nc = []
        for x in candidates:
            for y in mp[out]:
                if x[:7] == y[3:]:
                    nc.append(y[:3] + x)
        candidates = nc

    print(sorted(lmap(lambda x: int(x, 2), candidates))[0])

    # def combo(op):
    #     if op <= 3:
    #         return op
    #     if op <= 6:
    #         return regs[op - 4]
    # for i in range(pow(8, 15), pow(8, 16)):
    #     out = []
    #     regs = [i] + regs_orig[1:]
    #     ip = 0
    #     print((i - pow(8, 15)) / (pow(8, 16) - pow(8, 15)) * 100, '%')
    #     os.system('clear')
    #     while True:
    #         if ip + 1 >= len(programs):
    #             break
    #         op = programs[ip + 1]
    #         match programs[ip]:
    #             case 0:
    #                 regs[0] //= 1 << combo(op)
    #             case 1:
    #                 regs[1] ^= op
    #             case 2:
    #                 regs[1] = combo(op) % 8
    #             case 3:
    #                 if regs[0] != 0:
    #                     ip = op - 2
    #             case 4:
    #                 regs[1] = regs[1] ^ regs[2]
    #             case 5:
    #                 v = combo(op) % 8
    #                 out.append(v)

    #                 if len(out) > len(programs) or v != programs[len(out) - 1]:
    #                     break
    #             case 6:
    #                 regs[1] = regs[0] // (1 << combo(op))
    #             case 7:
    #                 regs[2] = regs[0] // (1 << combo(op))
    #         ip += 2
    #     print(out)
    #     if len(out) == len(programs) and all(map(lambda t: t[0] == t[1], zip(out, programs))):
    #         print('ans = ', i)
    #         break

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 2
r"""
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
