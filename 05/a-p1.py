import sys; sys.dont_write_bytecode = True; from utils import *
from itertools import takewhile
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

    rules = lmap(lambda s: ints(s), takewhile(lambda line: line, lines))


    def test(updates: list) -> bool:
        nodes = set(updates)
        updates = deque(updates)
        out_edges = {key: [] for key in nodes}
        for rule in rules:
            if rule[0] not in nodes:
                continue
            out_edges[rule[0]].append(rule[1])

        indeg = {key: 0 for key in nodes}
        for n in out_edges:
            for m in out_edges[n]:
                if m not in nodes:
                    continue
                indeg[m] += 1

        q = deque(filter(lambda k: not indeg[k], indeg.keys()))

        while q:
            n = q.popleft()
            if not updates:
                return True
            if updates[0] == n:
                updates.popleft()
            for m in out_edges[n]:
                if m not in nodes:
                    continue
                indeg[m] -= 1
                if not indeg[m]:
                    q.append(m)
        return not updates

    ans = 0
    for line in lines:
        updates = ints(line)
        if test(updates):
            print(updates)
            ans += updates[len(updates) // 2]
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""], do_case)
