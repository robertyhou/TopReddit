import requests.auth
import time

class Authorizer():
    def __init__(self, limit=100, subreddit='popular', mode='top', t='day'):
        self.subreddit = subreddit
        self.mode = mode
        self.t = t
        self.url = 'https://oauth.reddit.com/r/'+self.subreddit+'/' + self.mode + '.json?t='+self.t+'&limit='
        self.JSON_page_list = []
        if limit <= 100:
            self.simple_request(limit)
        else:
            self.multiple_requests(limit)

    def simple_request(self, limit = 100):
        self.url += str(limit)
        client_auth = requests.auth.HTTPBasicAuth('15umy6vmCIHQ7A', 'uQgAoXAeOV6r6S3AKc9V8i7fFQU')
        post_data = {"grant_type": "password", "username": "ssf2130", "password": "github"}
        headers = {"User-Agent": "TopReddit/0.1 by ssf2130"}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                 headers=headers)
        token = response.json()['access_token']
        self.headers = {"Authorization": "bearer " + token,
                   "User-Agent": "TopReddit/0.1 by ssf2130"}

        request_JSON = requests.get(self.url, headers=self.headers).json()
        self.JSON_page_list.append(request_JSON)
        self.after = request_JSON['data']['after']

    def multiple_requests(self, limit=200):
        self.simple_request(100)
        limit -= 100
        while limit > 100:
            self.url = 'https://oauth.reddit.com/r/'+self.subreddit+'/' + self.mode + '.json?t='+self.t+'&limit=100&after=' + self.after
            request_JSON = requests.get(self.url, headers=self.headers).json()
            self.JSON_page_list.append(request_JSON)
            self.after = request_JSON['data']['after']
            limit -= 100
            time.sleep(0.25)
        if 0 < limit <= 100:
            self.url = 'https://oauth.reddit.com/r/'+self.subreddit+'/' + self.mode + '.json?t='+self.t+'&limit=' + str(limit) + "&after=" + self.after
            request_JSON = requests.get(self.url, headers=self.headers).json()
            self.JSON_page_list.append(request_JSON)
    def get_subreddit(self):
        return self.subreddit

    def getJSON(self):
        return self.JSON_page_list

    def get_time(self):
        return self.t
