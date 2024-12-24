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
    # x_i ^ y_i = a_i (i >= 1, else x_00 ^ y_00 = z_00)
    # x_i & y_i = b_i
    # a_i & d_i-1 = c_i (i >= 1)
    # b_i | c_i = d_i
    # a_i ^ d_i-1 = z_i (i >= 1)
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

    is_b_or_c = set()
    for i1, _, i2, _, _ in b_or_c:
        is_b_or_c.add(i1)
        is_b_or_c.add(i2)
    for x1, _, _, _, res in x_and_y:
        if res in is_b_or_c:
            d[res] = 'b' + x1[1:]
            is_b_or_c.remove(res)
        else:
            print("{0} is one of the swapped, should be b{1}".format(res, x1[1:]))
            # print('b{} is not found'.format(x1[1:]))
    for i1, _, i2, _, _ in b_or_c:
        if i1 in d and d[i1].startswith('b'):
            d[i2] = 'c' + d[i1][1:]
        elif i2 in d and d[i2].startswith('b'):
            d[i1] = 'c' + d[i2][1:]

    is_a_or_d = set()
    for i1, _, i2, _, _ in a_and_d:
        is_a_or_d.add(i1)
        is_a_or_d.add(i2)
    for x1, _, _, _, res in x_xor_y:
        if res in is_a_or_d:
            d[res] = 'a' + x1[1:]
            is_a_or_d.remove(res)
        elif x1[1:] != '00':
            print("{0} is one of the swapped".format(res))
    for o1, _, o2, _, maybe_dx in a_and_d:
        if o1 in d and d[o1].startswith('a'):
            d[o2] = 'd{:02}'.format(int(d[o1][1:]) - 1)
        elif o2 in d and d[o2].startswith('a'):
            d[o1] = 'd{:02}'.format(int(d[o2][1:]) - 1)
    nlines = []
    for line in lines:
        nline = [None] * 5
        for i in [0, 2, 4]:
            if line[i] in d:
                line[i] = d[line[i]]
        nline[1], nline[3], nline[4] = line[1], line[3], line[4]
        i1, i2 = line[0], line[2]
        i1, i2 = tuple(sorted([i1, i2]))
        nline[0], nline[2] = i1, i2
        nlines.append(nline)
    for i1, op, i2, arrow, o in sorted(nlines):
        if op == 'XOR' and \
           ((i1.startswith('x') and i2 == 'y' + i1[1:] and (o == 'a' + i1[1:] or (i1[1:] == '00' and o == 'z00'))) or \
            (i1.startswith('a') and i2 == 'd{:02}'.format(int(i1[1:]) - 1) and o == 'z' + i1[1:])):
            continue
        if op == 'OR' and \
           (i1.startswith('b') and i2 == 'c' + i1[1:] and o == 'd' + i1[1:]):
            continue
        if op == 'AND' and \
           (i1.startswith('x') and i2 == 'y' + i1[1:] and o == 'b' + i1[1:] or \
            i1.startswith('a') and i2 == 'd{:02}'.format(int(i1[1:]) - 1) and o == 'c' + i1[1:]):
            continue
        print(' '.join([i1, op, i2, arrow, o]))

    for k in d:
        if d[k] == 'd16':
            print('d16 <- ', k)
        elif d[k] == 'c31':
            print('c31 <- ', k)
        elif d[k] == 'b37':
            print('b37 <- ', k)
        elif d[k] == 'b21':
            print('b21 <- ', k)
    # (z37, rrn), rqf, nnr, (fkb, z16), (z31, rdn)
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
