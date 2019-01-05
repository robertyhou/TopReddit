from Authorizer import Authorizer
import matplotlib.pyplot as plt
import numpy as np

class Parser:
    def __init__(self,limit=100):
        authorizer = []
        authorizer.append(Authorizer(limit, subreddit='all', t='hour'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='hour'))
        authorizer.append(Authorizer(limit, subreddit='all', t='day'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='day'))
        authorizer.append(Authorizer(limit, subreddit='all', t='week'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='week'))
        authorizer.append(Authorizer(limit, subreddit='all', t='month'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='month'))
        authorizer.append(Authorizer(limit, subreddit='all', t='year'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='year'))
        authorizer.append(Authorizer(limit, subreddit='all', t='all'))
        authorizer.append(Authorizer(limit, subreddit='popular', t='all'))

        self.mode_dict = {}
        self.count_dict = {}

        for mode in authorizer:
            request_JSON = mode.getJSON()
            type = mode.get_subreddit()+mode.get_time()
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

            subReddits = []
            counts = []
            for dict in sorted_dictionary:
                subReddits.append(dict[1])
                counts.append(dict[0])

            self.mode_dict[type] = subReddits
            self.count_dict[type] = counts
    def plot(self):
        for key, value in self.mode_dict.items():
            objects = self.mode_dict[key][:10]
            y_pos = np.arange(len(objects))
            performance = self.count_dict[key][:10]


            plt.bar(y_pos, performance, align='center', alpha=0.5)
            plt.tight_layout()
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
            plt.savefig('app/static/'+key+'.png')
            plt.clf()
            plt.cla()
            plt.close()


if __name__ == '__main__':
    parser = Parser()
    parser.plot()
