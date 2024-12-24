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
    d = dict()
    zs = set()
    for known in itertools.takewhile(lambda x: x, lines):
        a, b = known.split(': ')
        d[a] = bool(int(b))
    lines = [line.split(' ') for line in lines]
    for line in lines:
        for x in line:
            if x.startswith('z'):
                zs.add(x)

    while any(map(lambda z: z not in d, zs)):
        for l, op, r, _, res in lines:
            if l in d and r in d:
                d[res] = calc(d[l], op, d[r])
    ans = 0
    for i in range(len(zs) - 1, -1, -1):
        ans = (ans << 1) + d['z' + '{:02}'.format(i)]
    print(ans)

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
