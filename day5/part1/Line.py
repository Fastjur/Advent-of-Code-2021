from dataclasses import dataclass

from Point import Point


@dataclass
class Line:
    start: Point
    end: Point

    @classmethod
    def from_points_array(cls, points: [Point, Point]):
        x1 = min(points[0].x, points[1].x)
        x2 = max(points[0].x, points[1].x)
        y1 = min(points[0].y, points[1].y)
        y2 = max(points[0].y, points[1].y)
        return Line(Point(x1, y1), Point(x2, y2))

    def get_all_points_on_line(self) -> [Point]:
        points = [
            Point(i, j)
            for j in range(self.start.y, self.end.y + 1)
            for i in range(self.start.x, self.end.x + 1)
        ]
        return points

