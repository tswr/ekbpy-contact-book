# -*- coding: utf-8 -*-

# Добавление нового приложения: http://vk.com/apps.php?act=add
# Созданное приложение ekbpy-contact-book: http://vk.com/editapp?id=2795678
# Авторизация: http://vk.com/pages?oid=-1&p=Авторизация_клиентских_приложений
# Выполнение запросов: http://vk.com/pages?oid=-1&p=Выполнение_запросов_к_API
# Метод получение контактов друзей: http://vk.com/pages?oid=-1&p=friends.get

import urllib2
import json
import webbrowser
import urlparse
from modules.parser import Parser

class VKontakte(Parser):
    """
    Класс для импорта контактов из VKontakte.
    """
    appId = 2795678
    redirectURI = "http://oauth.vkontakte.ru/blank.html"

    type_name_for_people = "Вконтакте"
    contactMapping = {
        "name" : "first_name",
        "additionalName" : None,
        "familyName" : "last_name",
        "nickname" : "nickname",
        "birthday" : "bdate",
        "gender" : "sex",
        "email" : None,
        "phone" : "mobile_phone",
        "address" : None,
        "organization" : None,
        "website" : None,
        "skype" : None,
        "vkontakte" : "uid",
        "icq" : None,
        "facebook" : None,
        "twitter" : None,
        "moikrug" : None
    }

    def __init__(self, authorizationResponse):
        """
        authorizationResponse - строка вида
        access_token=099ec13146323349098727e156092dc47e0090709076ce24a936f3b7e347bb5&expires_in=86400&user_id=10071505
        которую пользователь копирует из браузера после завершения авторизации в VKontakte.
        """
        responseDict = urlparse.parse_qs(authorizationResponse)
        #print responseDict
        self.userId = responseDict["user_id"][0]
        self.expiresIn = responseDict["expires_in"][0]
        self.accessToken = responseDict["access_token"][0]

    @staticmethod
    def authorize():
        """
        Открывает браузер с необходимой страницей на vkontakte для прохождения пользователем процесса авторизации.
        """
        settings = "friends"
        display = "popup"
        requestURI = "http://oauth.vkontakte.ru/authorize?client_id={0}&scope={1}&redirect_uri={2}&display={3}&response_type=token".format(VKontakte.appId, settings, VKontakte.redirectURI, display)
        #print requestURI
        webbrowser.open_new(requestURI)

    @staticmethod
    def callAPI(method, params, accessToken):
        """
        Используется для вызова api функций. Возвращает json, преобразованный в объектное представление.
        """
        targetURI = "https://api.vkontakte.ru/method/{0}?{1}&access_token={2}".format(method, params, accessToken)
        vk = urllib2.urlopen(targetURI)
        response = vk.read()
        return json.loads(response)

    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        #fields = "uid,first_name,last_name,nickname,sex,bdate,city,country,timezone,photo,photo_medium,photo_big,domain,has_mobile,rate,contacts,education"
        fieldsList = ["uid", "first_name", "last_name", "nickname", "sex", "bdate", "contacts", "mobile_phone"]
        fields = ",".join(fieldsList)
        name_case = "nom"
        params = "uid={0}&fields={1}&name_case={2}".format(self.userId, fields, name_case)
        o = VKontakte.callAPI("getFriends", params, self.accessToken)
        for user in o["response"]:
            if "uid" in user:
                user["uid"] = "http://vk.com/id{0}".format(user["uid"])
            if "mobile_phone" in user:
                user["mobile_phone"] = self.makePretty(user["mobile_phone"])
            if "sex" in user:
                pass
        return o["response"]

if __name__ == "__main__":
    VKontakte.authorize()
    authorizationResponse = raw_input("Enter the response of vk.com after your authorization: ")
    vk = VKontakte(authorizationResponse)
    print vk.getFriends()
