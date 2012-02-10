#-*- coding:utf-8 -*-

from Contact import Contact
from modules.importGoogle import Google
from modules.importThunderbird import Thunderbird
from modules.importVkontakte import VKontakte
from modules.importFacebook import Facebook
from modules.importMoiKrug import MoiKrug

def contactsListFromProvider(provider):
    """
    Функция зовет у провайдера метод getFriends() и 
    используя статическую переменную contactMapping из класса провайдера
    делает из списка словарей список контактов.
    """
    friends = provider.getFriends()
    contacts = []
    for f in friends:
        fields = {}
        for k,v in f.iteritems():
            fields[k] = v
        c = Contact(**fields)
        contacts.append(c)
    return contacts

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
