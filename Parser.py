from Authorizer import Authorizer
url = 'https://oauth.reddit.com/r/all/hot.json?limit=100'

authorizer = Authorizer(url)
text = authorizer.getJSON()
children = text['data']['children']
for child in children:
    print(child['data']['subreddit'])