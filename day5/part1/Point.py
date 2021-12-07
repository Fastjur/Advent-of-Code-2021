from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_coords_array_str(cls, xy: [str, str]):
        return Point(int(xy[0]), int(xy[1]))