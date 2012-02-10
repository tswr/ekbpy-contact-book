#-*- coding:utf-8 -*-

class Contact(object):
    """
    Контакты
    описывает всевозможные поля контактов человека
    отвечает за импорт и экспорт ( с помощью модулей ) контакта в различные типы
    импорт и экспорт по сути это всего лишь преобразование названий полей.
    """
    # поля контактов
    fieldNames = [ "name",
                   "additionalName",
                   "familyName",
                   "nickname",
                   "birthday",
                   "gender",
                   "email",
                   "phone",
                   "address",
                   "organization",
                   "website",
                   "skype",
                   "vkontakte",
                   "icq",
                   "facebook",
                   "twitter",
                   "moikrug"]

    def __init__(self, **kwargs):
        for f in self.fieldNames:
            self.__dict__[f] = kwargs.get(f, "")
        self._id = kwargs.get("_id", None)

    def __str__(self):
        return str({field:self.__dict__[field]
                        for field in self.fieldNames
                                if self.__dict__[field]})
        
    def _name_icontains(self, pattern):
        return self.name.upper().__contains__(pattern.upper())
    
    def _familyname_icontains(self, pattern):
        return self.familyName.upper().__contains__(pattern.upper())
    
    def _additionalname_icontains(self, pattern):
        return self.additionalName.upper().__contains__(pattern.upper())
    
    def filter_by_name(self, pattern=""):
        return self._name_icontains(pattern) or self._familyname_icontains(pattern) or self._additionalname_icontains(pattern)
