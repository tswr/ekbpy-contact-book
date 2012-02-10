# -*- coding: utf-8 -*-

# Добавление нового приложения: http://vk.com/apps.php?act=add
# Созданное приложение ekbpy-contact-bk: https://developers.facebook.com/apps/251812358229762/summary?save=1
# Авторизация: https://developers.facebook.com/docs/authentication/
# Выполнение запросов: https://developers.facebook.com/docs/reference/api/

import urllib2
import json
import webbrowser
import urlparse
from modules.parser import Parser

class Facebook(Parser):
    """
    Класс для импорта контактов из Facebook.
    """
    appId = 251812358229762
    appSecret = "db70382205ef8b45a798d4ed6ce785e1"
    redirectURI = "https://www.facebook.com/connect/login_success.html"

    contactMapping = {
        "name" : "first_name",
        "additionalName" : None,
        "familyName" : "last_name",
        "nickname" : None,
        "birthday" : "birthday",
        "gender" : "gender",
        "email" : None,
        "phone" : "mobile_phone",
        "address" : None,
        "organization" : None,
        "website" : "website",
        "skype" : None,
        "vkontakte" : "uid",
        "icq" : None,
        "facebook" : "link",
        "twitter" : None,
        "moikrug" : None
    }

    def __init__(self, authorizationResponse):
        """
        authorizationResponse - строка вида
        access_token=AAADlBaIpjwIBAJTkQXWzu2u5Sw0rD6ZBzzFA6pnwkMZBJPV8gNFFLSyeXHwcyZAg1nDcUUwudKNsaQdQEpd373bxi77ihkaWao5e4pNCAZDZD&expires_in=6441
        которую пользователь копирует из браузера после завершения авторизации в Facebook.
        """
        raise NotImplementedError

    @staticmethod
    def authorize():
        """
        Открывает браузер с необходимой страницей на facebook для прохождения пользователем процесса авторизации.
        """
        scope = "friends_about_me,friends_birthday,friends_website"
        responseType = "token"
        requestURI = "https://www.facebook.com/dialog/oauth?client_id={0}&scope={1}&response_type={2}&redirect_uri={3}".format(
                Facebook.appId, scope, responseType, Facebook.redirectURI)
        raise NotImplementedError

    @staticmethod
    def callAPI(method, params, accessToken):
        """
        Используется для вызова api функций. Возвращает json, преобразованный в объектное представление.
        """
        targetURI = "https://graph.facebook.com/{0}?params={1}&access_token={2}".format(method, params, accessToken)
        raise NotImplementedError

    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        raise NotImplementedError
