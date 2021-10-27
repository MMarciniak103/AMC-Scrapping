import stweet as st
import pandas as pd
import json
import arrow
from tqdm import tqdm

def run_search(since, until, hashtag="#koronawirus"):
    search_tweets_task = st.SearchTweetsTask(all_words=hashtag,since=since,until=until)
    output_jl_tweets = st.JsonLineFileRawOutput(f'{hashtag[1:]}_tweets.json')
    output_jl_users = st.JsonLineFileRawOutput(f'{hashtag[1:]}_users.json')
    st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                         tweet_raw_data_outputs=[output_jl_tweets],
                         user_raw_data_outputs=[output_jl_users]).run()
        

if __name__ == "__main__":
    start = arrow.get(2020, 1, 1)
    end = arrow.utcnow().shift(hours=2)
    
    generator = arrow.Arrow.span_range('week', start, end)
    for (since, until) in tqdm(generator):
        run_search(since, until, hashtag="#ekstraklasa")   