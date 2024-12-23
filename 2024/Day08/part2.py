def parse_input(raw_input):
    return [list(row) for row in raw_input.strip().split("\n")]

def get_antenna_types(input_data):
    antenna_types = {}
    for i, row in enumerate(input_data):
        for j, char in enumerate(row):
            if char == '.':
                continue
            if char not in antenna_types:
                antenna_types[char] = []
            antenna_types[char].append((i, j))
    return antenna_types

def get_valid_antinode_locations(start, end, antenna1, antenna2, input_data):
    distance = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
    valid_locations = []

    for x in range(start, end):
        locations = [
            (antenna1[0] + distance[0] * x, antenna1[1] + distance[1] * x),
            (antenna2[0] - distance[0] * x, antenna2[1] - distance[1] * x),
        ]

        for loc in locations:
            if 0 <= loc[0] < len(input_data) and 0 <= loc[1] < len(input_data[0]):
                valid_locations.append(loc)

    return valid_locations

def solve_part_2(raw_input):
    input_data = parse_input(raw_input)
    antenna_types = get_antenna_types(input_data)
    
    antinodes = set()
    
    for antennas in antenna_types.values():
        for i, antenna1 in enumerate(antennas):
            for j in range(i + 1, len(antennas)):
                antenna2 = antennas[j]
                valid_antinodes = get_valid_antinode_locations(0, len(input_data), antenna1, antenna2, input_data)

                for antinode in valid_antinodes:
                    antinodes.add(antinode)

    return len(antinodes)

if __name__ == "__main__":
    raw_input = """
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

result = solve_part_2(raw_input)
print("Result:", result)
