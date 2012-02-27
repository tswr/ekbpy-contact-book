# -*- coding: utf-8 -*-

import re

def validate(phoneString):
    """
    Проверяет, является ли переданная строка телефоном в формате +12345678901.
    Возвращает True, если является, False иначе.
    """
    #return len(phoneString) == 12 and re.search(r'^\+[0-9]{11}$', phoneString) is not None
    return re.search(r'^\+[0-9]{11}$', phoneString) is not None

def makePretty(phoneString):
    """
    Извлекает из произвольной строки телефон и возвращает его в формате, удовлетворяющем validate.
    """
    phone = re.sub(r"[^+0-9]", "", phoneString)
    if len(phone) == 10:
        phone = "+7" + phone
    phone = re.sub(r"^8", "+7", phone)
    return phone if validate(phone) else ""

##############
# unit tests #
##############

import unittest

class PhoneTestCase(unittest.TestCase):

    def test_validate_1(self):
        test = "qwerasdfzxcv"
        expectedRes = False
        self.assertEqual(validate(test), expectedRes)

    def test_validate_2(self):
        test = "+12345678901"
        expectedRes = True
        self.assertEqual(validate(test), expectedRes)

    def test_validate_3(self):
        test = " +12345678901 "
        expectedRes = False
        self.assertEqual(validate(test), expectedRes)

    def test_validate_4(self):
        test = "+7(900)000-00-00"
        expectedRes = False
        self.assertEqual(validate(test), expectedRes)

    def test_makePretty_1(self):
        test = "qwerasdfzxcv"
        expectedRes = ""
        self.assertEqual(makePretty(test), expectedRes)

    def test_makePretty_2(self):
        test = "My phone is: +1(234)567-890-1 lalala"
        expectedRes = "+12345678901"
        self.assertEqual(makePretty(test), expectedRes)

    def test_makePretty_3(self):
        test = "81234567890"
        expectedRes = "+71234567890"
        self.assertEqual(makePretty(test), expectedRes)

    def test_makePretty_4(self):
        test = "8 (123) 456 dash 78 dash 90"
        expectedRes = "+71234567890"
        self.assertEqual(makePretty(test), expectedRes)

    def test_makePretty_5(self):
        test = "8 (123) 456 dash 78"
        expectedRes = ""
        self.assertEqual(makePretty(test), expectedRes)

    def test_makePretty_6(self):
        test = "(343) 3-10-10-10"
        expectedRes = "+73433101010"
        self.assertEqual(makePretty(test), expectedRes)

if __name__ == "__main__":
    unittest.main()
