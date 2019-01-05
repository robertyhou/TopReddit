from Authorizer import Authorizer
import matplotlib.pyplot as plt
import numpy as np

class Parser:
    def __init__(self, limit=100, subreddit='all', t='day'):
        authorizer = Authorizer(limit, subreddit=subreddit, t=t)
        self.subreddit = subreddit
        self.time = t
        request_JSON = authorizer.getJSON()
        sub_count = {}
        for text in request_JSON:
            children = text['data']['children']
            for child in children:
                child_subreddit = child['data']['subreddit']
                if child_subreddit in sub_count:
                    sub_count[child_subreddit] += 1
                else:
                    sub_count[child_subreddit] = 1

        sorted_dictionary = sorted((value, key) for (key, value) in sub_count.items())[::-1]

        self.top_subreddits = []
        self.counts = []
        for key in sorted_dictionary:
            self.top_subreddits.append(key[1])
            self.counts.append(key[0])

    def plot(self):
        subreddits = self.top_subreddits[:10]
        y_pos = np.arange(len(subreddits))
        number_of_occurrence = self.counts[:10]
        for n in range(len(subreddits)):
            if len(subreddits[n]) > 10:
                subreddits[n] = subreddits[n][:10] + '...'
        plt.bar(y_pos, number_of_occurrence, align='center', alpha=0.5)

        plt.xticks(y_pos, subreddits, fontsize=8)
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
        plt.title('Top 10 Subreddits of '+self.time+' in /r/'+self.subreddit)
        plt.tight_layout()
        plt.savefig('app/static/graph.png')
        plt.gcf().clear()

if __name__ == '__main__':
    parser = Parser()
    parser.plot()
