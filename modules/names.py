# -*- coding: utf-8 -*-

def splitString(string):
    """
    Используется для выделения имени и фамилии из данной строки.
    Отбрасываются лишние пробелы, берутся первое и последнее слова в строке.
    На выходе tuple из двух строк: имени и фамилии.
    """
    list = string.split()
    llen = len(list)
    first = list[0] if llen > 0 else ''
    last = list[llen - 1] if llen > 1 else ''
    return (first, last)

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
