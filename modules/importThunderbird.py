# -*- coding: utf-8 -*-

import codecs
from modules.parser import Parser

class Thunderbird(Parser):
    """
    Класс для импорта контактов из локального csv файла, полученного через экспорт первого круга из moikrug в формате
    thunderbird.
    """
    type_name_for_people = "Thunderbird"
    contactMapping = {
        "name" : "name1",
        "additionalName" : "name2",
        "familyName" : "Family Name",
        "nickname" : None,
        "birthday" : None,
        "gender" : None,
        "email" : "Primary Email",
        "phone" : "Mobile Number",
        "address" : None,
        "organization" : None,
        "website" : None,
        "skype" : None,
        "vkontakte" : None,
        "icq" : None,
        "facebook" : None,
        "twitter" : None,
        "moikrug" : None
    }

    def __init__(self, csvFileName):
        """
        csvFileName - имя файла, из которого необходимо произвести импорт
        """
        self.csvFileName = csvFileName

    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        contacts = []
        with codecs.open(self.csvFileName, encoding='cp1251') as f:
            contacts = self.CSVParse(f)
            for c in contacts:
                if "Display Name" in c:
                    c["name1"], c["name2"] = self.splitString(c["Display Name"])
                if "Mobile Number" in c:
                    c["Mobile Number"] = self.makePretty(c["Mobile Number"])
        return contacts

if __name__ == "__main__":
    print Thunderbird("thunderbird.csv").getFriends()
