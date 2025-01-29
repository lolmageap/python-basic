pt1 = (1.0, 2.0)
pt2 = (4.0, 2.5)

from math import sqrt

len1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

pt3 = Point(1.0, 2.0)
pt4 = Point(4.0, 2.5)

Point2 = namedtuple("Point2", "x y z")
Point3 = namedtuple("Point3", "x, y, z")

temp_dict = {"x": 1, "y": 2, "z": 3}

pt5 = Point2(**temp_dict)

Classes = namedtuple("Classes", ["number", "rank"])

numbers = [str(i) for i in range(1, 21)]
ranks = ["A", "B", "C", "D"]

students = [Classes(rank, number) for rank in ranks for number in numbers]

if __name__ == "__main__":
    print(pt3)
    print(pt4)
    print(pt5)
    print(pt5._fields)
    print(pt5._asdict())
    print(students)