# -*- coding: utf-8 -*-

import codecs
from modules.parser import Parser

class Thunderbird(Parser):
    """
    Класс для импорта контактов из локального csv файла, полученного через экспорт первого круга из moikrug в формате
    thunderbird.
    """
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
        raise NotImplementedError

    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        raise NotImplementedError
