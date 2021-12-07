from dataclasses import dataclass

from Point import Point


@dataclass
class Line:
    start: Point
    end: Point

    @classmethod
    def from_points_array(cls, points: [Point, Point]):
        return Line(points[0], points[1])

    def get_all_points_on_line(self) -> [Point]:
        x_step = 1 if self.start.x < self.end.x else -1
        y_step = 1 if self.start.y < self.end.y else -1
        range_x = range(self.start.x, self.end.x + x_step, x_step)
        range_y = range(self.start.y, self.end.y + y_step, y_step)

        if self.start.x == self.end.x or self.start.y == self.end.y:
            points = [
                Point(i, j)
                for j in range_y
                for i in range_x
            ]
        else:
            diagonal_line_length = len(range_x)
            points = [
                Point(i * x_step + self.start.x, i * y_step + self.start.y)
                for i in range(diagonal_line_length)
            ]
        print(points)
        return points

