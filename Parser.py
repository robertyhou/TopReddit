'''
https://www.reddit.com/r/all/hot.json?limit=100

'''
import urllib.request, json
url = 'https://www.reddit.com/r/all/hot.json?limit=500'
jsonurl = urllib.request.urlopen(url)
text = json.loads(jsonurl.read())
children = text['data']['children']
countDict = {}
for child in children:
    subreddit = child['data']['subreddit']
    if subreddit not in countDict:
        countDict[subreddit] = 1
    else:
        countDict[subreddit] += 1
print(countDict)
