# -*- coding: utf-8 -*-

import re

def validate(phoneString):
    """
    Проверяет, является ли переданная строка телефоном в формате +12345678901.
    Возвращает True, если является, False иначе.
    """
    
    if phoneString[0]=='+':
		b=phoneString[1:]
		if len(b) <> 11:
			return False
		for s in b:
			if int(s) not in [1,2,3,4,5,6,7,8,9,0]:
				return False
		return True
    else:
		return False
#    raise NotImplementedError

def makePretty(phoneString):
    """
    Извлекает из произвольной строки телефон и возвращает его в формате, удовлетворяющем validate.
    """
    phone=''
    for s in xrange(0,len(phoneString)):
		if phoneString[s]  in ['+','1','2','3','4','5','6','7','8','9','0']:
			phone=phone+phoneString[s]
    if len(phone)==0:
		return ''
    if len(phone)==10:
		phone='+7'+phone
    if phone[0] == '8':
		phone='+7'+phone[1:]
    if not validate(phone):
		phone=''		
    return phone
			


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
