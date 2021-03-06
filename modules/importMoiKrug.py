# -*- coding: utf-8 -*-

# Добавление нового приложения: https://oauth.yandex.ru/client/new
# Созданное приложение: https://oauth.yandex.ru/client/aff62db3ea564801972eb9131d77dafd
# Авторизация: http://api.yandex.ru/oauth/doc/dg/reference/obtain-access-token.xml
# Выполнение запросов: http://api.yandex.ru/moikrug/doc/dg/concepts/operations.xml

import urllib2
import json
import webbrowser
from modules.parser import Parser

class MoiKrug(Parser):
    """
    Класс для импорта контактов из MoiKrug.
    """
    client_id = "aff62db3ea564801972eb9131d77dafd"
    client_secret = "1d9a4f61dea445d2bbe3cc75c143e9b6"

    contactMapping = {
        "name" : "name1",
        "additionalName" : None,
        "familyName" : "name2",
        "nickname" : None,
        "birthday" : None,
        "gender" : "gender",
        "email" : None,
        "phone" : None,
        "address" : None,
        "organization" : None,
        "website" : None,
        "skype" : None,
        "vkontakte" : None,
        "icq" : None,
        "facebook" : None,
        "twitter" : None,
        "moikrug" : "link"
    }

    def __init__(self, authorizationCode):
        """
        authorizationCode - код авторизации, который был показан пользователю в браузере.
        """
        dataString = "grant_type=authorization_code&code={0}&client_id={1}&client_secret={2}".format(authorizationCode, MoiKrug.client_id, MoiKrug.client_secret)
        r = urllib2.urlopen("https://oauth.yandex.ru/token", dataString)
        if r.getcode() != 200:
            raise Exception("HTTP code " + r.getcode() + " " + r.readlines())
        ans = r.readlines()[0]
        self.access_token = json.loads(ans)['access_token']


    @staticmethod
    def authorize():
        """
        Открывает браузер с необходимой страницей на moikrug для прохождения пользователем процесса авторизации.
        """
        client_id = "aff62db3ea564801972eb9131d77dafd"
        response_type = "code"
        display = "popup"
        requestURI = "https://oauth.yandex.ru/authorize?response_type={0}&client_id={1}&display={2}".format(response_type, client_id, display)
        webbrowser.open(requestURI)

    @staticmethod
    def openFriends(access_token):
        friendsGetURI = "http://api.moikrug.ru/v1/{0}/?oauth_token={1}&{2}".format("my/friends", access_token, "")
        return urllib2.urlopen(friendsGetURI)


    @staticmethod
    def callAPI(method, params, access_token):
        """
        Используется для вызова api функций. Возвращает json, преобразованный в объектное представление.
        """

        friendsGetURI = "http://api.moikrug.ru/v1/{0}/?oauth_token={1}&{2}".format(method, access_token, params)
        r = urllib2.urlopen(friendsGetURI)
        if r.getcode() != 200:
            raise Exception("Response code: " + r.getcode() + " " + r.readlines())
        return json.loads(r.read())


    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        friendsIds = MoiKrug.callAPI("my/friends", "", self.access_token)
        idsList = ','.join(friendsIds)
        friends = MoiKrug.callAPI("person", "ids=" + idsList, self.access_token)
        for f in friends:
            f['name2'], f['name1'] = self.splitString(f['name'])
        return friends
