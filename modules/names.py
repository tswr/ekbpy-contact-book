# -*- coding: utf-8 -*-

def splitString(string):
    """
    Используется для выделения имени и фамилии из данной строки.
    Отбрасываются лишние пробелы, берутся первое и последнее слова в строке.
    На выходе tuple из двух строк: имени и фамилии.
    """
    a = string.strip().split()
    if len(a) >= 2:
        return a[0], a[-1]
    if len(a) == 1:
        return a[0], ""
    else:
        return "", ""

##############
# unit tests #
##############

import unittest

class NamesTestCase(unittest.TestCase):

    def test_short(self):
        test = ""
        expectedRes = "", ""
        self.assertEqual(splitString(test), expectedRes)

    def test_normal(self):
        test = "  Asdf     Qwer   "
        expectedRes = "Asdf", "Qwer"
        self.assertEqual(splitString(test), expectedRes)

    def test_long(self):
        test = "  Asdf  zxcv jkl;   Qwer   "
        expectedRes = "Asdf", "Qwer"
        self.assertEqual(splitString(test), expectedRes)

if __name__ == "__main__":
    unittest.main()
