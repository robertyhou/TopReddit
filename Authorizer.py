import requests.auth

class Authorizer():
    def __init__(self, url):
        client_auth = requests.auth.HTTPBasicAuth('15umy6vmCIHQ7A', 'uQgAoXAeOV6r6S3AKc9V8i7fFQU')
        post_data = {"grant_type": "password", "username": "ssf2130", "password": "github"}
        headers = {"User-Agent": "TopReddit/0.1 by ssf2130"}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                 headers=headers)
        token = response.json()['access_token']
        headers = {"Authorization": "bearer " + token,
                   "User-Agent": "TopReddit/0.1 by ssf2130"}

        self.response = requests.get(url, headers=headers)
    def getJSON(self):
        return self.response.json()
