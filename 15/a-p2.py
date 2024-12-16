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
    CHAR_TO_DELTA = {
        "^": [-1, 0],
        ">": [0, 1],
        "v": [1, 0],
        "<": [0, -1]
    }

    lines = iter(inp.splitlines())
    g = lmap(lambda s: list(s), takewhile(lambda l: l, lines))
    for i in range(len(g)):
        nrow = []
        for ch in g[i]:
            if ch == 'O':
                nrow += ['[', ']']
            elif ch == '#':
                nrow += ['#', '#']
            else:
                nrow.append(ch)
                nrow.append('.')
        g[i] = nrow

    G = Grid(g)
    dirs = ''.join(lines)
    start = None
    for coord in G.coords():
        if G[coord] == '@':
            start = coord
            break

    pos = start
    def pair(pos):
        if G[pos] == '[' :
            return padd(pos, [0, 1])
        elif G[pos] == ']':
            return padd(pos, [0, -1])

    def check(pos, d) -> bool:
        cur = padd(pos, d)
        if not G.in_bounds(*cur) or G[cur] == '#':
            return False
        if G[cur] == '.':
            return True
        cur_pair = pair(cur)
        return check(cur, d) and check(cur_pair, d)

    def move(cur, d):
        nxt = padd(cur, d)
        if not G.in_bounds(*nxt) or G[nxt] == '#':
            print("???????????????", cur, d)
            return
        if G[nxt] == ']' or G[nxt] == '[':
            nxt_pair = pair(nxt)
            move(nxt, d)
            move(nxt_pair, d)
        G[nxt] = G[cur]
        G[cur] = '.'
    for ch in dirs:
        d = CHAR_TO_DELTA[ch]
        if ch == '<' or ch == '>':
            cur = padd(pos, d)
            while G.in_bounds(*cur) and (G[cur] == '[' or G[cur] == ']'):
                cur = padd(cur, d)
            if G.in_bounds(*cur) and G[cur] == '.':
                while cur != pos:
                    nxt = psub(cur, d)
                    G[cur] = G[nxt]
                    cur = nxt
                G[pos] = '.'
                pos = padd(pos, d)
        else:
            if check(pos, d):
                move(pos, d)
                pos = padd(pos, d)

    ans = 0
    for coord in G.coords():
        if G[coord] == '[':
            ans += coord[0] * 100 + coord[1]
    print(ans)
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""", r"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""",r"""
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
