from pprint import pprint

from Point import Point
from Line import Line
from OceanFloor import OceanFloor

if __name__ == "__main__":
    f = open("../input.txt", "r")
    input_lines = f.readlines()

    lines = [
        line
        for line
        in [
            Line.from_points_array([
                Point.from_coords_array_str(p.split(","))
                for p
                in input_line.strip().split(" -> ")
            ])
            for input_line
            in input_lines
        ]
        if line.start.x == line.end.x or line.start.y == line.end.y
    ]
    pprint(lines)

    ocean_floor = OceanFloor(lines)
    print(ocean_floor.count_overlap_points())
