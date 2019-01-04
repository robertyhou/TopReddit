from Authorizer import Authorizer


def temp():
    url = 'https://oauth.reddit.com/r/popular/top.json?limit=100'


    authorizer = Authorizer(url)
    text = authorizer.getJSON()
    children = text['data']['children']
    subCount = {}
    counter = 0
    for child in children:
        subReddit = child['data']['subreddit']
        if subReddit in subCount:
            subCount[subReddit] += 1
        else:
            subCount[subReddit] = 1
        counter += 1
    print(counter)
    print(subCount)

    sorted_dictionary = sorted((value, key) for (key, value) in subCount.items())[::-1]

    subReddits = []
    counts = []
    for dict in sorted_dictionary:
        subReddits.append(dict[1])
        counts.append(dict[0])

    import matplotlib.pyplot as plt;

    plt.rcdefaults()
    import numpy as np

    objects = subReddits[:10]
    y_pos = np.arange(len(objects))
    performance = counts[:10]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.xticks(rotation=25)
    plt.ylabel('Count')
    plt.title('Top Subreddits of the Day')

    plt.savefig('app/static/graph.png')

temp()
