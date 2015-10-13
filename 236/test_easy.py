#! python

import unittest
import easy
import collections

class test_bag(unittest.TestCase):
    def setUp(self):
        self.pieces = ["O", "I", "S", "Z", "L", "J", "T"]

    def test_seven(self):
        bag = easy.bag(self.pieces)
        test_list = self.pieces[:]
        for piece in bag:
            test_list.remove(piece)
        self.assertFalse(test_list)


class test_finite_bag(unittest.TestCase):

    def setUp(self):
        self.pieces = ["O", "I", "S", "Z", "L", "J", "T"]

    def test_14(self):
        bag = easy.finite_bag(14, self.pieces)
        result = collections.Counter(bag)
        for k, v in result.iteritems():
            self.assertEqual(v, 2)

    def test_50(self):
        bag = easy.finite_bag(50, self.pieces)
        result = collections.Counter(bag)
        eight = False
        for _, v in result.iteritems():
            try:
                self.assertEqual(v, 7)
            except AssertionError as error:
                if not eight:
                    self.assertEqual(v, 8)
                    eight = True
                else:
                    raise error


if __name__ == '__main__':
    unittest.main()
