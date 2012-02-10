#-*- coding:utf-8 -*-

import Contact
import distance
import translit

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
                    "moikrug"]
    # Лениво делать, когда-нибудь потом
    sameAsGroups = [["name",
                     "additionalName",
                     "familyName"]]
    maybeFields = ["nickname",
                   "familyName"]
    def isFieldsMergable(x,y):
        """ Определяет возможно ли мержить поля автоматически"""
        return (not x) or (not y) or (x == y)

    def isFieldsSeemsMergable(x,y):
        """ Определяет, что поля возможно похожи """
        return x == y or distance.levenshtein(x,y) < 3
        
    fullSimiliarity    = False
    partialSimiliarity = False
    for field in sameAsFields:
        fullSimiliarity = \
            fullSimiliarity or isFieldsMergable(
                contact1.__dict__[field],
                contact2.__dict__[field])
        
    for field in contact1.fieldNames:
        if field in maybeFields:
            partialSimiliarity =\
                partialSimiliarity or isFieldsSeemsMergable(
                    contact1.__dict__[field],
                    contact2.__dict__[field])
        fullSimiliarity = \
            fullSimiliarity and isFieldsMergable(
                contact1.__dict__[field],
                contact2.__dict__[field])
            
    if fullSimiliarity:
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
        c1 = Contact.Contact(name="Dmitri", familyName=u"Корнев")
        c2 = Contact.Contact(name=u"Дмитрий", familyName="Kornev")
        self.assertEqual(areMergeable(c1, c2), 1)

    def test_areMergeable_9(self):
        c1 = Contact.Contact(name="Dmitriy", familyName=u"Корнев")
        c2 = Contact.Contact(name=u"Дмитрий", familyName="Kornev")
        self.assertEqual(areMergeable(c1, c2), 2)

if __name__ == "__main__":
    unittest.main()
