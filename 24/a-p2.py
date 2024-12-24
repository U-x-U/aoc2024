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

def calc(a, op, b):
    if op == 'AND':
        return a and b
    if op == 'OR':
        return a or b
    assert(op == 'XOR')
    return a ^ b
def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = iter(inp.splitlines())
    xs, ys, zs = [0] * 45, [0] * 45, [0] * 46
    for known in itertools.takewhile(lambda x: x, lines):
        a, b = known.split(': ')
        if a.startswith('x'):
            xs[int(a[1:])] = int(b)
        if a.startswith('y'):
            ys[int(a[1:])] = int(b)

    d = dict()
    lines = [line.split(' ') for line in lines]

    # adder:
    # x_i ^ y_i = a_i (i >= 1. x_00 ^ y_00 = z_00)
    # x_i & y_i = b_i (i >= 1. x_00 & y_00 = d_00, b.c. there's no c_00)
    # a_i & d_i-1 = c_i (i >= 1)
    # b_i | c_i = d_i (i <= 44. b_44 | c_44 = z45)
    # a_i ^ d_i-1 = z_i (i >= 1, i <= 44)
    # ONLY output may be swapped, so inputs are always correct
    x_xor_y = list(filter(lambda line: line[1] == 'XOR' and (line[0].startswith('x') or line[0].startswith('y')), lines))
    x_and_y = list(filter(lambda line: line[1] == 'AND' and (line[0].startswith('x') or line[0].startswith('y')), lines))
    a_and_d = list(filter(lambda line: line[1] == 'AND' and not (line[0].startswith('x') or line[0].startswith('y')), lines))
    b_or_c = list(filter(lambda line: line[1] == 'OR', lines))
    a_xor_d = list(filter(lambda line: line[1] == 'XOR' and not (line[0].startswith('x') or line[0].startswith('y')), lines))

    for eq in x_xor_y:
        if eq[0].startswith('y'):
            eq[0], eq[2] = eq[2], eq[0]
    for eq in x_and_y:
        if eq[0].startswith('y'):
            eq[0], eq[2] = eq[2], eq[0]

    # all inputs of "OR" gate is either b or c.
    # use this to check output of "x_i and y_i"
    is_b_or_c = {i for i1, _, i2, _, _ in b_or_c for i in (i1, i2)}
    for x1, _, _, _, res in x_and_y:
        if res in is_b_or_c:
            d[res] = 'b' + x1[1:]
        elif x1[1:] != '00':
            print("{0} is one of the swapped, should be b{1}".format(res, x1[1:]))
    for i1, _, i2, _, _ in b_or_c:
        if i1 in d and d[i1].startswith('b'):
            d[i2] = 'c' + d[i1][1:]
        elif i2 in d and d[i2].startswith('b'):
            d[i1] = 'c' + d[i2][1:]

    # all non-x-non-y inputs of "AND" gate is either a or d.
    # use this to check output of "x_i xor y_i"
    is_a_or_d = {i for i1, _, i2, _, _ in a_and_d for i in (i1, i2)}
    for x1, _, _, _, res in x_xor_y:
        if res in is_a_or_d:
            d[res] = 'a' + x1[1:]
        elif x1[1:] != '00':
            print("{0} is one of the swapped, should be a{1}".format(res, x1[1:]))
    for o1, _, o2, _, _ in a_and_d:
        if o1 in d and d[o1].startswith('a'):
            d[o2] = 'd{:02}'.format(int(d[o1][1:]) - 1)
        elif o2 in d and d[o2].startswith('a'):
            d[o1] = 'd{:02}'.format(int(d[o2][1:]) - 1)
    nlines = []
    for line in lines:
        nline = [d.get(line[0], line[0]), line[1], d.get(line[2], line[2]), line[3], d.get(line[4], line[4])]
        nline[0], nline[2] = sorted([nline[0], nline[2]])
        nlines.append(nline)
    for i1, op, i2, arrow, o in sorted(nlines):
        if op == 'XOR' and  i1 == 'x00' and i2 == 'y00' and o == 'z00' or \
           op == 'AND' and  i1 == 'x00' and i2 == 'y00' and o == 'd00' or \
           op == 'OR' and i1 == 'b44' and i2 == 'c44' and o == 'z45':
            continue
        if op == 'XOR' and i1.startswith('x') and i2 == 'y' + i1[1:]:
            if o != 'a' + i1[1:]:
                print('{0}, output should be a{1}'.format(' '.join([i1, op, i2, arrow, o]), i1[1:]))
        elif op == 'XOR' and i1.startswith('a') and i2 == 'd{:02}'.format(int(i1[1:]) - 1):
            if o != 'z' + i1[1:]:
                print('{0}, output should be z{1}'.format(' '.join([i1, op, i2, arrow, o]), i1[1:]))
        elif op == 'OR' and i1.startswith('b') and i2 == 'c' + i1[1:]:
            if o != 'd' + i1[1:]:
                print('{0}, output should be d{1}'.format(' '.join([i1, op, i2, arrow, o]), i1[1:]))
        elif op == 'AND' and i1.startswith('x') and i2 == 'y' + i1[1:]:
            if o != 'b' + i1[1:]:
                print('{0}, output should be b{1}'.format(' '.join([i1, op, i2, arrow, o]), i1[1:]))
        elif op == 'AND' and i1.startswith('a') and i2 == 'd{:02}'.format(int(i1[1:]) - 1):
            if o != 'c' + i1[1:]:
                print('{0}, output should be c{1}'.format(' '.join([i1, op, i2, arrow, o]), i1[1:]))

    for k in d:
        if d[k] == 'd16':
            print('d16 <- ', k)
        elif d[k] == 'c31':
            print('c31 <- ', k)
    # prints (after reordering and clustering)
    # z37 is one of the swapped, should be b37
    # a37 XOR d36 -> rrn, output should be z37
    # x37 AND y37 -> z37, output should be b37
    #
    # rqf is one of the swapped, should be b21
    # nnr is one of the swapped, should be a21
    # x21 AND y21 -> rqf, output should be b21
    # x21 XOR y21 -> nnr, output should be a21
    #
    # a16 XOR d15 -> d16, output should be z16
    # b16 OR c16 -> z16, output should be d16
    #
    # a31 AND d30 -> z31, output should be c31
    # a31 XOR d30 -> c31, output should be z31
    #
    #
    # d20 is not inferenced b.c. a21 is swapped. d20 is hvv.
    # b20 OR c20 -> hvv, output should be d20
    #
    # c37 is not inferenced b.c. b37 is swapped. c37 is vhj.
    # a37 AND d36 -> vhj, output should be c37
    #
    # c31 <-  rdn
    # d16 <-  fkb
    # (z37, rrn), (rqf, nnr), (fkb, z16), (z31, rdn)
    print(','.join(sorted(['z37', 'rrn', 'rqf', 'nnr', 'fkb', 'z16', 'z31', 'rdn'])))

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
