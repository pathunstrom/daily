def point(string):
    string = string[1:-1]
    points = string.split(",")
    return float(points[0]), float(points[1])


def point_list(f):
    return [point(p) for p in f.read().splitlines()[1:]]
