import pandas as pd
import praw

my_client_id = "[...]"
my_client_secret = "[...]"
my_user_agent = "CMNS801_research_project"

reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret,
                     user_agent=my_user_agent)

df_rows = []


# collect top posts from r/health

# get comments from a specified submission
def get_comments(submission_id):
    submission = reddit.submission(id=submission_id)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        df_rows.append([comment.id, comment.score,
                        comment.created, comment.body])
    print(f"Added ~ {len(submission.comments)} comments")


if __name__ == '__main__':
    df_input = pd.read_csv('data/top_health_posts.csv')
    submission_ids = df_input.id.tolist()
    for submission_id in submission_ids:
        get_comments(submission_id)
    df_output = pd.DataFrame(df_rows, columns=[
        'comment_id', 'comment_score', 'comment_created', 'comment_body'])
    df_output.to_csv('data/comments_from_top_health_posts.csv')
