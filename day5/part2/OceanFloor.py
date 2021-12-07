from Line import Line


class OceanFloor:
    lines: [Line]
    max_x: int
    max_y: int
    map: [[int]]

    def __init__(self, lines: [Line]):
        self.lines = lines
        self.max_x = max([item for sublist in map(lambda line: [line.start.x, line.end.x], lines) for item in sublist])
        self.max_y = max([item for sublist in map(lambda line: [line.start.y, line.end.y], lines) for item in sublist])
        self.map = [[0 for _ in range(self.max_x + 1)] for _ in range(self.max_y + 1)]

        for line in self.lines:
            points_on_line = line.get_all_points_on_line()
            for point in points_on_line:
                self.map[point.y][point.x] = self.map[point.y][point.x] + 1

        print(self.str())

    def str(self) -> str:
        string = ""
        for y in self.map:
            for x in y:
                string = string + x.__str__()
            string = string + '\n'

        return string

    def count_overlap_points(self) -> int:
        count = 0
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                if self.map[y][x] > 1:
                    count = count + 1
        return count
