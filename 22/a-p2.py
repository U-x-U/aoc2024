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
#In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:
    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
#
# Each step of the above process involves mixing and pruning:
    # To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation.
        # (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    # To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation.
        # (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)

def mix_prune(num, x):
    num ^= x
    num %= 16777216
    return num
def get_prices(line: str):
    num = int(line)
    ans = [num % 10]
    for _ in range(2000):
        mul = num * 64
        num = mix_prune(num, mul)
        div = num // 32
        num = mix_prune(num, div)
        mul2 = num * 2048
        num = mix_prune(num, mul2)
        ans.append(num % 10)
    return ans

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    prices = lmap(get_prices, lines)
    changes = lmap(list_diff, prices)
    s2bs = []
    seqset = set()
    # calc a Map (seq2bestprice) for each buyer
    for price, change in zip(prices, changes):
        s2b = dict()
        for seq, p in zip(windows(change, 4), price[4:]):
            seq = tuple(seq)
            # READ carefully:
            #     the monkey will only look for a specific sequence of four consecutive changes in price,
            #     then IMMEDIATELY sell WHEN it sees that sequence.
            # Below is not correct:
            #     s2b.setdefault(seq, 0)
            #     s2b[seq] = max(s2b[seq], p)
            if seq not in s2b:
                s2b[seq] = p
            seqset.add(seq)
        s2bs.append(s2b)
    ans = 0
    bestseq = None
    for seq in seqset:
        sm = 0
        for s2b in s2bs:
            if seq in s2b:
                sm += s2b[seq]
        if sm > ans:
            bestseq = seq
        ans = max(ans, sm)
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
1
10
100
2024
""",r"""
1
2
3
2024
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)