# -*- coding: utf-8 -*-

import re

gp_find = re.compile(r'\w+', re.LOCALE)

def splitString(string):
    """
    Используется для выделения имени и фамилии из данной строки.
    Отбрасываются лишние пробелы, берутся первое и последнее слова в строке.
    На выходе tuple из двух строк: имени и фамилии.
    """
    ll_res = gp_find.findall(string)
    lv_res_len = len(ll_res)
    
    if lv_res_len > 1:
	lt_out = (ll_res[0], ll_res[-1])
    elif lv_res_len == 1:
	lt_out = (ll_res[0], '')
    else:
	lt_out = ('', '')
	
    return lt_out

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
