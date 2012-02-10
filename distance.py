# -*- coding: utf-8 -*-

def levenshtein(s1, s2):
    """
    Вычисляет расстояние Левенштейна для двух заданных строк.
    """
    raise NotImplementedError

##############
# unit tests #
##############

import unittest

class DistanceTestCase(unittest.TestCase):

    def test_levenshtein_1(self):
        self.assertEqual(levenshtein("asdf", "asde"), 1)

    def test_levenshtein_2(self):
        self.assertEqual(levenshtein("asdf", "asd"), 1)

    def test_levenshtein_3(self):
        self.assertEqual(levenshtein("asdf", "asdfe"), 1)

    def test_levenshtein_4(self):
        self.assertEqual(levenshtein("asdf", "adfe"), 2)

    def test_levenshtein_5(self):
        self.assertEqual(levenshtein("kitten", "sitting"), 3)

    def test_levenshtein_6(self):
        self.assertEqual(levenshtein("Saturday", "Sunday"), 3)

    def test_levenshtein_7(self):
        self.assertEqual(levenshtein(u"проверка", u"программы"), 6)

if __name__ == "__main__":
    unittest.main()
