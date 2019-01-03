'''
https://www.reddit.com/r/all/hot.json?limit=100

'''
import urllib.request, json
url = 'https://www.reddit.com/r/all/hot.json?limit=100'
jsonurl = urllib.request.urlopen(url)
text = json.loads(jsonurl.read())
children = text['data']['children']
for child in children:
    print(child['data']['subreddit'])