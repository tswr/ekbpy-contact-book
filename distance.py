# -*- coding: utf-8 -*-

def levenshtein(s1, s2):
    """
    Вычисляет расстояние Левенштейна для двух заданных строк.
    """
    if s1 == s2:
        return 0
    slen, dlen = len(s1), len(s2)
    dist = [[0 for i in range(dlen+1)] for x in range(slen+1)]
    for i in xrange(slen+1):
        dist[i][0] = i
    for j in range(dlen+1):
        dist[0][j] = j
    for i in range(slen):
        for j in xrange(dlen):
            cost = 0 if s1[i] == s2[j] else 1
            dist[i+1][j+1] = min(
                dist[i][j+1] + 1,
                dist[i+1][j] + 1,
                dist[i][j] + cost
            )
    return dist[-1][-1]

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
