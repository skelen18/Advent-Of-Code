def parse_input(input_data):
    grid = input_data.strip().splitlines()
    antennas = []
    height = len(grid)
    width = len(grid[0])
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != ".":
                antennas.append((x, y, cell))
    return antennas, width, height


def find_antinodes(antennas, width, height):
    antinodes = set()
    for i, (x1, y1, freq1) in enumerate(antennas):
        for j, (x2, y2, freq2) in enumerate(antennas):
            if i >= j or freq1 != freq2:
                continue
            dx, dy = x2 - x1, y2 - y1
            antinode1_x, antinode1_y = x1 - dx, y1 - dy
            if 0 <= antinode1_x < width and 0 <= antinode1_y < height:
                antinodes.add((antinode1_x, antinode1_y))
            antinode2_x, antinode2_y = x2 + dx, y2 + dy
            if 0 <= antinode2_x < width and 0 <= antinode2_y < height:
                antinodes.add((antinode2_x, antinode2_y))
    return antinodes


def main(input_data):
    antennas, width, height = parse_input(input_data)
    antinodes = find_antinodes(antennas, width, height)
    print(f"Result: {len(antinodes)}")

input_data = """
.........................p........................
......................h....C............M.........
..............................p....U..............
..5..................p............................
..6z...........................................C..
...............c...........zV.....................
...5.....c........................................
.Z.............h........S...z....9................
.O............................9...z........M..C...
..O....5..............................F..M..C.....
..Z.........5.c...............M....V..............
........ZO................q.......................
s...O................h..Uq.....7V...........4.....
.q.g..............c.............p.......4.........
............hZ.............................4G.....
6s...........................U.Q.....3............
.......6.................9.......Q.............3..
....s..D.........................6................
.............................................FL...
..................................................
..g...D.........q.....f.......Q...F....L......7...
...............2.........f.............V.L...4....
...................2.s...................f3......G
....g...........................v......7P.........
..2..g.............d.....v...........P.......1....
..............u.........f.............L........G..
.........l.D....u...............d........o..P.....
..................8...............9..1......o...7.
............l.....................................
...................l...S...........F.......o..U...
.......................u...S......................
..........l....u...............m...........P....G.
......................................1.8.......o.
..................................................
..................v.......S................0......
.............v........d.....1.....................
..................................................
..........D....................................0..
...................m.............H..........0.....
...................................d......0.......
..................................................
....Q.............................................
................................H................. 
........................H....................8....
..................................................
..................................................
.........................................8........
.......................H3.........................
............................m.....................
................................m.................
"""

main(input_data)
