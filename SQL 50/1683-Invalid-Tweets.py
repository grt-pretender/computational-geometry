# 1683. Invalid Tweets

# tweet_id is the primary key (column with unique values) for this table.
# This table contains all the tweets in a social media app.
 
# Write a solution to find the IDs of the invalid tweets. 
# The tweet is invalid if the number of characters used in the content 
# of the tweet is strictly greater than 15.
# Return the result table in any order.

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    invalid_tweets = tweets[tweets['content'].str.len() > 15]
    result_df = invalid_tweets[['tweet_id']]
    return result_df