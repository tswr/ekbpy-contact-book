#-*- coding:utf-8 -*-

def fromRussian(input):
    """
    Транслитерирует символы русских букв. Остальные символы оставляет неизмененными.
    """
    translationTable = {
        u"а" : "a",    u"А" : "A",  
        u"б" : "b",    u"Б" : "B",  
        u"в" : "v",    u"В" : "V",  
        u"г" : "g",    u"Г" : "G",  
        u"д" : "d",    u"Д" : "D",  
        u"е" : "e",    u"Е" : "E", 
        u"ё" : "yo",   u"Ё" : "Yo", 
        u"ж" : "zh",   u"Ж" : "Zh", 
        u"з" : "z",    u"З" : "Z",  
        u"и" : "i",    u"И" : "I",  
        u"й" : "y",    u"Й" : "Y",  
        u"к" : "k",    u"К" : "K",  
        u"л" : "l",    u"Л" : "L",  
        u"м" : "m",    u"М" : "M",  
        u"н" : "n",    u"Н" : "N",  
        u"о" : "o",    u"О" : "O",  
        u"п" : "p",    u"П" : "P",  
        u"р" : "r",    u"Р" : "R",  
        u"с" : "s",    u"С" : "S",  
        u"т" : "t",    u"Т" : "T",  
        u"у" : "u",    u"У" : "U",  
        u"ф" : "f",    u"Ф" : "F",  
        u"х" : "kh",   u"Х" : "Kh", 
        u"ц" : "ts",   u"Ц" : "Ts", 
        u"ч" : "ch",   u"Ч" : "Ch", 
        u"ш" : "sh",   u"Ш" : "Sh", 
        u"щ" : "sch",  u"Щ" : "Sch",
        u"ъ" : "'",    u"Ъ" : "'",  
        u"ы" : "y",    u"Ы" : "Y",  
        u"ь" : "'",    u"Ь" : "'",  
        u"э" : "e",    u"Э" : "E",  
        u"ю" : "yu",   u"Ю" : "Yu", 
        u"я" : "ya",   u"Я" : "Ya", 
        u" " : " "
    }

    result = ""
    for letter in input:
        if letter in translationTable :
            result += translationTable[unicode(letter)]
        else :
            result += letter
    return result


##############
# unit tests #
##############

import unittest

class TranslitTestCase(unittest.TestCase):

    def test_fromRussian_1(self):
        self.assertEqual(fromRussian(u"Проверка Asdf Связи"), u"Proverka Asdf Svyazi")

    def test_fromRussian_2(self):
        self.assertEqual(fromRussian(u"Дмитрий theShockwaveRider Корнев"), u"Dmitriy theShockwaveRider Kornev")

if __name__ == "__main__":
    unittest.main()
