#-*- coding:utf-8 -*-

from Contact import Contact
from modules.importGoogle import Google
from modules.importThunderbird import Thunderbird
from modules.importVkontakte import VKontakte
from modules.importFacebook import Facebook
from modules.importMoiKrug import MoiKrug

def contactsListFromProvider(provider):
    """
    Функция зовет у провайдера метод getFriends() и используя статическую переменную contactMapping из класса провайдера
    делает из списка словарей список контактов.
    """
    cls = provider.__class__
    friends = provider.getFriends()
    contactList = []
    for friend in friends:
        dictionary = {}
        for field in Contact.fieldNames:
            if field in cls.contactMapping \
               and cls.contactMapping[field] is not None \
               and cls.contactMapping[field] in friend:
                dictionary[field] = friend[cls.contactMapping[field]]
        newContact = Contact(**dictionary)
        contactList.append(newContact)
    return contactList

def importFromGoogleCSV(fileName):
    return contactsListFromProvider(Google(fileName))

def importFromThunderbirdCSV(fileName):
    return contactsListFromProvider(Thunderbird(fileName))

def importFromVKontakte_authorize():
    VKontakte.authorize()

def importFromVKontakte(authorizationResponse):
    return contactsListFromProvider(VKontakte(authorizationResponse))

def importFromFacebook_authorize():
    Facebook.authorize()

def importFromFacebook(authorizationResponse):
    return contactsListFromProvider(Facebook(authorizationResponse))

def importFromMoiKrug_authorize():
    MoiKrug.authorize()

def importFromMoiKrug(authorizationCode):
    return contactsListFromProvider(MoiKrug(authorizationResponse))
