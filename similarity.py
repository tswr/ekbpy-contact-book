#-*- coding:utf-8 -*-

import Contact
import distance
import translit

class InvalidRelation(Exception):
    pass

def areMergeable(contact1, contact2):
    """
    Определяет, нужно ли объединить два контакта.
    Возвращает 0, если объединять нельзя
    Возвращает 1, если нужно предложить объединение пользователю
    Возвращает 2, если можно объединить в автоматическом режиме
    """
    sameAsFields = ["email",
                    "phone",
                    "icq",
                    "skype",
                    "vkontakte",
                    "facebook",
                    "twitter",
                    "moikrug",
                    "familyName"]
    # Лениво делать, когда-нибудь потом
    sameAsGroups = [["name",
                     "additionalName",
                     "familyName"]]
    maybeFields = ["nickname",
                   "familyName"]

    def isFieldsEqual(x,y):
        """ Определяет эквивалентность полей """
        x_translit, y_translit = map(translit.fromRussian, (x, y))
        return (x_translit == y_translit) and x and y

    def isFieldsMergable(x,y):
        """ Определяет возможно ли мержить поля автоматически"""
        x_translit, y_translit = map(translit.fromRussian, (x, y))
        return (not x) or (not y) or (x_translit == y_translit)

    def isFieldsSeemsMergable(x,y):
        """ Определяет, что поля возможно похожи """
        return x and (x == y or distance.levenshtein(x,y) <= 3)

    ANY, ALL = 1, 2
    def checkFields(fieldSet, checker, unionType):
        """ Осуществляет проверку набора полей fieldSet чекером checker.
            Результаты проверки полей объединяются по отношению unionType.
            В этой функции ещё есть куда стремиться. """
        if unionType == ANY:
            out = False
        elif unionType == ALL:
            out = True
        else:
            raise InvalidRelation()
        for field in fieldSet:
            x,y = contact1.__dict__[field], contact2.__dict__[field]
            if unionType == ANY:
                out = out or checker(x,y)
            if unionType == ALL:
                out = out and checker(x,y)
        return out

    allFields = contact1.fieldNames
    
    # Схожесть должна проявляться хотя бы в одном поле из заданного набора
    canAutomatic        = checkFields(sameAsFields, isFieldsEqual,         ANY)

    # Сращиваемыми должны быть все поля
    fullSimiliarity     = checkFields(allFields,    isFieldsMergable,      ALL)
    
    # Похожесть должна наблюдаться хотя бы в одном поле из заданного набора
    partialSimiliarity  = checkFields(maybeFields,  isFieldsSeemsMergable, ANY)  
            
    if fullSimiliarity and canAutomatic:
        return 2
    if partialSimiliarity:
        return 1
    return 0

##############
# unit tests #
##############

import unittest

class SimilarityTestCase(unittest.TestCase):

    def test_areMergeable_1(self):
        c1 = Contact.Contact(name="Asdf", email="test@email")
        c2 = Contact.Contact(familyName="Qwer", email="test@email")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_2(self):
        c1 = Contact.Contact(name="Asdf", phone="+12345678901")
        c2 = Contact.Contact(familyName="Qwer", phone="+12345678901")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_3(self):
        c1 = Contact.Contact(name="Pasha", vkontakte="1")
        c2 = Contact.Contact(familyName="Tot samiy", vkontakte="1")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_4(self):
        c1 = Contact.Contact(name="Mark", facebook="1")
        c2 = Contact.Contact(familyName="Tot samiy", facebook="1")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_5(self):
        c1 = Contact.Contact(name="Asdf", moikrug="url")
        c2 = Contact.Contact(familyName="Qwer", moikrug="url")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_6(self):
        c1 = Contact.Contact(name="Asdf", moikrug="url")
        c2 = Contact.Contact(familyName="Qwer", moikrug="url")
        self.assertEqual(areMergeable(c1, c2), 2)

    def test_areMergeable_7(self):
        c1 = Contact.Contact(name="X")
        c2 = Contact.Contact(name="X")
        self.assertEqual(areMergeable(c1, c2), 0)

    def test_areMergeable_8(self):
        c1 = Contact.Contact(familyName="Asdf")
        c2 = Contact.Contact(familyName="Asdffff")
        self.assertEqual(areMergeable(c1, c2), 1)

    def test_areMergeable_9(self):
        c1 = Contact.Contact(name="Dmitriy", familyName=u"Корнев")
        c2 = Contact.Contact(name=u"Дмитрий", familyName="Kornev")
        self.assertEqual(areMergeable(c1, c2), 2)

if __name__ == "__main__":
    unittest.main()
