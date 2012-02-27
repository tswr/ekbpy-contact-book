#-*- coding:utf-8 -*-

import csvparser
import phone
import names

__type_name__ = ""

class Parser(object):
    """
    Родительский класс для всех классов-парсеров
    классы-наследники обязаны переопределить
    contactMapping - соответствие названий контактов внутреннее и ресурса
    getFriends - основной метод, возвращает друзей с ресурса
    type_name - имя типа, ресурса для использования в программном коде
    type_name_for_people - имя типа, ресурса для человека
    """
    type_name = __type_name__
    type_name_for_people = ""
    contactMapping = {}

    def getFriends(self):
        """
        Возвращает друзей с заданного ресурса
        """

    def CSVParse(self, fileHandle):
        return csvparser.CSVParse(fileHandle)

    def validate(self, phoneString):
        return phone.validate(phoneString)
    
    def makePretty(self, phoneString):
        return phone.makePretty(phoneString)

    def splitString(self, string):
        return names.splitString(string)
