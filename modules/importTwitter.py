# -*- coding: utf-8 -*-

import twitter
from modules.parser import Parser

class Twitter(Parser):
    """
    Класс для импорта контактов из Twitter.
    Получить реквизиты можно по адресу: https://dev.twitter.com
    """
    consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret=''

    contactMapping = {
        "name" : "name",
        "additionalName" : None,
        "familyName" : None,
        "nickname" : "screen_name",
        "birthday" : None,
        "gender" : None,
        "email" : None,
        "phone" : None,
        "address" : None,
        "organization" : None,
        "website" : None,
        "skype" : None,
        "vkontakte" : None,
        "icq" : None,
        "facebook" : None,
        "twitter" : "id",
        "moikrug" : None
    }

    def __init__(self, authorizationResponse):
        """
        authorizationResponse - строка вида
        access_token=099ec13146323349098727e156092dc47e0090709076ce24a936f3b7e347bb5&expires_in=86400&user_id=10071505
        которую пользователь копирует из браузера после завершения авторизации в VKontakte.
        consumer_{key, secret} авторизует разработчика (приложение)
        acess_token_{key, secret} - клиента (пользователя).
        Поскольку consumer_secret должен оставаться секретным, а в Python-проекте на GitHub это невозможно, пользователю
        следует зарегистрироваться как разработчику на Twitter.
        """
        api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

    @staticmethod
    def authorize():
        """
        Открывает браузер с необходимой страницей на vkontakte для прохождения пользователем процесса авторизации.
        """
        pass

    @staticmethod
    def callAPI(method, params, accessToken):
        """
        Используется для вызова api функций. Возвращает json, преобразованный в объектное представление.
        Для Twitter пуст, т.к. реализован сторонним модулем.
        """
        pass

    def _prune(u):
        """
        Закрытый метод, удаляющий ненужные поля из словаря пользователя
        """
        result = {}
        for k in contactMapping.keys():
            secondaryKey = contactMapping[k]
            if secondaryKey:
                result[secondaryKey] = u[secondaryKey]
        return result

    def getFriends(self):
        """
        Возвращает список словарей пользователей.
        """
        result = []
        for u in users:
            result.append(prune(u.AsDict()))
        return result
