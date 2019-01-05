from Authorizer import Authorizer
import matplotlib.pyplot as plt
import numpy as np

class Parser:
    def __init__(self, limit=100, subreddit='all', t='day'):
        authorizer = Authorizer(limit, subreddit=subreddit, t=t)
        request_JSON = authorizer.getJSON()
        subCount = {}
        for text in request_JSON:
            children = text['data']['children']
            for child in children:
                subReddit = child['data']['subreddit']
                if subReddit in subCount:
                    subCount[subReddit] += 1
                else:
                    subCount[subReddit] = 1

        sorted_dictionary = sorted((value, key) for (key, value) in subCount.items())[::-1]

        self.subReddits = []
        self.counts = []
        for dict in sorted_dictionary:
            self.subReddits.append(dict[1])
            self.counts.append(dict[0])


    def plot(self):
        objects = self.subReddits[:10]
        y_pos = np.arange(len(objects))
        performance = self.counts[:10]
        for n in range(len(objects)):
            if len(objects[n]) > 10:
                objects[n] = objects[n][:10] + '...'
        plt.bar(y_pos, performance, align='center', alpha=0.5)

        plt.xticks(y_pos, objects, fontsize=8)
        ax = plt.gca()
        ax.set_aspect(aspect=0.2)
        pad = 5
        for tick in ax.xaxis.get_major_ticks()[0:]:
            tick.set_pad(pad)
            if pad < 20:
                pad += 10
            elif pad > 20:
                pad = 5

        plt.ylabel('Count')
        plt.title('Top Subreddits of the Day')
        plt.tight_layout()
        plt.savefig('app/static/graph.png')
        plt.gcf().clear()

if __name__ == '__main__':
    parser = Parser()
    parser.plot()
