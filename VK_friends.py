# from urllib.parse import urlencode
# APP_ID = 1111111
#
# OAUTH_API_BASE_URL = 'https://oauth.vk.com/authorize'
#
# REDIRECT_URI = 'https://oauth.vk.com/blank.html'
#
# SCOPE = 'friends'
#
# OAUTH_PARAMS = {
#     'redirect_uri': REDIRECT_URI,
#     'scope': SCOPE,
#     'response_type': 'token',
#     'client_id': APP_ID
# }
#
# print('?'.join([OAUTH_API_BASE_URL, urlencode(OAUTH_PARAMS)]))

import requests
from urllib.parse import urljoin
from pprint import pprint

TOKEN = '----token----'
API_BASE_URL = 'https://api.vk.com/method/'
V = '5.21'

# id пользователей, у которых нужно найти общих друзей
FIRST_ID = '----id----'
SECOND_ID = '----id----'


class VKAPIClient:
    # BASE_URL = API_BASE_URL
    def __init__(self, id_user, token=TOKEN, version=V):
        self.token = token
        self.version = version
        self.id_user = id_user


    def friends_get_id(self):
        friends_get_id = urljoin(API_BASE_URL, 'friends.get')
        response = requests.get(friends_get_id, params={
            'access_token': self.token,
            'v': self.version,
            'user_id': self.id_user,
        })
        return response.json()['response']['items']


    def __and__(self, other):
        return set(user1.friends_get_id()) & set(user2.friends_get_id())

    def get_profile(self):
        get_profile = urljoin('https://vk.com/', 'id' + self.id_user)
        return get_profile



if __name__ == '__main__':
    user1 = VKAPIClient(FIRST_ID)
    user2 = VKAPIClient(SECOND_ID)
    # Вписать "id", чтобы получить ссылку на профиль
    user_profile = VKAPIClient('----id----')
    user = user_profile.get_profile()
    print(user1 & user2)
    print(user)




