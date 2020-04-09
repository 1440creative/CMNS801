import pandas as pd
import praw
import time

my_client_id = "[...]"
my_client_secret = "[...]"
my_user_agent = "CMNS801_research_project"

reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret,
                     user_agent=my_user_agent)

# collect top posts from r/health


def collect_posts():
    start_time = time.time()
    posts = []
    print('Starting scrape...')
    hot_posts = reddit.subreddit('News').hot(
        time_filter='month', limit=None)
    for post in hot_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.url,
                      post.num_comments, post.selftext, post.created])
        df = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit',
                                          'url', 'num_comments', 'body', 'created'])
        df.to_csv('data/top_health_posts.csv')
    print(f'Scraped {len(posts)} in {time.time() - start_time}')


# execute
if __name__ == '__main__':
    collect_posts()
