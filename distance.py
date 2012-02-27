# -*- coding: utf-8 -*-

def levenshtein(s1, s2):
    """
    Вычисляет расстояние Левенштейна для двух заданных строк.
    """
    l1 = len(s1)
    l2 = len(s2)
    matrix = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1):
        matrix[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2):
        for sz in range(0,l1):
            if s1[sz] == s2[zz]:
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
            else:
                matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
    return matrix[l2][l1]


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
