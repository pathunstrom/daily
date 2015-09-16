import unittest
import solution
import os

class TestPoints(unittest.TestCase):

    def setUp(self):
        self.input = os.path.relpath('gold.txt')

    def test_parsing_tuples(self):
        with open(self.input, 'r') as f:
            points = f.read().splitlines()
        first_point = points[1]
        second_point = points[2]
        third_point = points[3]
        self.assertEqual(solution.point(first_point), (6.422011725438139, 5.833206713226367))
        self.assertEqual(solution.point(second_point), (3.154480546252892, 4.063265532639129))
        self.assertEqual(solution.point(third_point), (8.894562467908552, 0.3522346393034437))

    def test_getting_point_list(self):
        with open(self.input, 'r') as f:
            points = solution.point_list(f)
        point_list = [(6.422011725438139, 5.833206713226367),
                      (3.154480546252892, 4.063265532639129),
                      (8.894562467908552, 0.3522346393034437),
                      (6.004788746281089, 7.071213090379764),
                      (8.104623252768594, 9.194871763484924),
                      (9.634479418727688, 4.005338324547684),
                      (6.743779037952768, 0.7913485528735764),
                      (5.560341970499806, 9.270388445393506),
                      (4.67281620242621, 8.459931892672067),
                      (0.30104230919622, 9.406899285442249),
                      (6.625930036636377, 6.084986606308885),
                      (9.03069534561186, 2.3737246966612515),
                      (9.3632392904531, 1.8014711293897012),
                      (2.6739636897837915, 1.6220708577223641),
                      (4.766674944433654, 1.9455404764480477),
                      (7.438388978141802, 6.053689746381798)]
        self.assertEqual(points, point_list)

    def test_sorted_points(self):
        pass