import pandas as pd


def main():
    tweets = {
        'tweet_id': [1, 2],
        'content': [
            'Let us Code',
            'More than fifteen chars are here!'
        ]
    }
    tweets_df = pd.DataFrame(tweets)
    result = invalid_tweets(tweets_df)
    print(result.to_string(index=False))


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]


if __name__ == '__main__':
    main()