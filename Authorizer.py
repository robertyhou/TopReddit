import requests.auth
import time
"""
Authenticates user on Reddit API using OAuth2
Obtains JSON of requested query
"""


class Authorizer():

    """
    Requests Reddit query in JSON format

    Keyword arguments:
    limit     -- number of posts (default 100)
    subreddit -- type of subreddit (default '/r/popular')
    mode      -- type of sorting (default 'top')
    t         -- time range (default 'day')
    """
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

    """Obtains JSON data for under 100 posts"""
    def simple_request(self, limit=100):
        self.url += str(limit)

        # client id, secret key (tied to application made with ssf2130)
        client_auth = requests.auth.HTTPBasicAuth('15umy6vmCIHQ7A', 'uQgAoXAeOV6r6S3AKc9V8i7fFQU')

        post_data = {"grant_type": "password", "username": "ssf2130", "password": "github"}
        headers = {"User-Agent": "TopReddit/0.1 by ssf2130"}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                                 headers=headers) #return response that gives access to reddit api
        token = response.json()['access_token'] #from the response, retrive the token which gives access
        self.headers = {"Authorization": "bearer " + token,
                   "User-Agent": "TopReddit/0.1 by ssf2130"} #user-agent is purpose

        request_JSON = requests.get(self.url, headers=self.headers).json() #json with reddit data used in parser
        self.JSON_page_list.append(request_JSON)
        self.after = request_JSON['data']['after'] #bookmark so that next request gives next 100

    """Obtains JSON data for over 100 posts"""
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

    """Returns type of subreddit"""
    def get_subreddit(self):
        return self.subreddit

    """Returns list of JSON data"""
    def getJSON(self):
        return self.JSON_page_list

    """Returns mode of time"""
    def get_time(self):
        return self.t
