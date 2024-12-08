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
    lines = inp.splitlines()
    lines = [list(line) for line in lines]
    g = Grid(lines)
    
    CHAR_TO_DELTA = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    NEXT_DELTA = {}
    CHARS = list(CHAR_TO_DELTA.keys())
    for c1, c2 in zip(CHARS, CHARS[1:] + [CHARS[0]]):
        NEXT_DELTA[CHAR_TO_DELTA[c1]] = CHAR_TO_DELTA[c2]

    def dfs(pos, d, visited):
        if (pos, d) in visited:
            return True
        visited.add((pos, d))
        npos = tuple(padd(pos, d))
        ret = True
        if g.in_bounds(*npos) and g[npos] != '#':
            ret &= dfs(npos, d, visited)
        elif g.in_bounds(*npos):
            nd = NEXT_DELTA[d]
            ret &= dfs(pos, nd, visited)
        else:
            return False
        return ret

    found = False
    start_pos = (0, 0)
    start_dir = (0, 0)
    visited = set()
    for i in range(g.rows):
        for j in range(g.cols):
            if g[[i, j]] in CHAR_TO_DELTA.keys():
                start_pos = (i, j)
                start_dir = CHAR_TO_DELTA[g[i, j]]
                dfs(start_pos, start_dir, visited)
                found = True
                break
        if found: break

    candidates = set([v[0] for v in visited])
    ans = 0
    for pos in candidates:
        if pos == start_pos:
            continue
        g[pos] = '#'
        if dfs(start_pos, start_dir, set()):
            ans += 1
        g[pos] = '.'

    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""], do_case)
