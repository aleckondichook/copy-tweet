from deta import app
import tweepy
import config

# api keys for tweepy
client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                       consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

# uses deta.sh to run the program on a schedule
@app.lib.cron()
def cron_task(event):
    # retrieve list of target tweets
    target_tweets = client.get_users_tweets(id="{}".format(config.TARGET_ID))

    # retrieve list of self tweets and initialize self array
    self_tweets = client.get_users_tweets(id="{}".format(config.SELF_ID))
    self_array = []
    for tweet in range(len(self_tweets[0])):
        self_array.append(self_tweets[0][tweet]['text'])

    # loop through target tweets backwards
    i = len(target_tweets[0]) - 1
    while i >= 0:
        # check if it is a new tweet
        if any(target_tweets[0][i]['text'][0:30] in j for j in self_array):
            print("not a new tweet")
        else:
            # check if the tweet was a quote tweet, if so remove ending
            # characters of tweet so quote tweet will fit in the 280 character limit
            if len(target_tweets[0][i]['text']) > 280:
                client.create_tweet(text=target_tweets[0][i]['text'][0:255] + " " + target_tweets[0][i]['text'][-23:])
            # check if the tweet is a retweet
            elif target_tweets[0][i]['text'][0:4] == "RT @":
                client.retweet(tweet_id=target_tweets[0][i]['id'])
            # send out the copied tweet
            else:
                client.create_tweet(text=target_tweets[0][i]['text'])
            print("tweeted new tweet starting with " + str(target_tweets[0][i]['text'][0:10]))
        i -= 1