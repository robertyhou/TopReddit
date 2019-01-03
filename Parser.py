from Authorizer import Authorizer
import pandas as pd
url = 'https://oauth.reddit.com/r/popular/hot.json?limit=1000'

authorizer = Authorizer(url)
text = authorizer.getJSON()
children = text['data']['children']
subCount = {}
for child in children:
    #print(child['data']['subreddit'])
    subReddit = child['data']['subreddit']
    if subReddit in subCount:
        subCount[subReddit] += 1
    else:
        subCount[subReddit] = 1
print(subCount)

subReddits = []
counts = []

for sub in subCount:
    subReddits.append(sub)
    counts.append(subCount[sub])

print(subReddits)
print(counts)

df = pd.DataFrame({'sub':subReddits, 'val':counts})
ax = df.plot.bar(x='lab', y='val', rot=0)
