# -*- coding: utf-8 -*-

import codecs
from modules.parser import Parser

class Google(Parser):
    """
    Класс для импорта контактов из локального csv файла, полученного через экспорт контактов gmail.
    """
    contactMapping = {
        "name" : "Given Name",
        "additionalName" : "Additional Name",
        "familyName" : "Family Name",
        "nickname" : "Nickname",
        "birthday" : "Birthday",
        "gender" : "Gender",
        "email" : "E-mail 1 - Value",
        "phone" : "Phone 1 - Value",
        "address" : "Address 1 - Formatted",
        "organization" : "Organization 1 - Name",
        "website" : "Website 1 - Value",
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
