import tweepy
from Tweet import Tweet
import datetime


class Crawler:
    def __init__(self, keyword, hours, language):
        self.keyword = keyword
        self.hours = hours
        self.lang = language
        self.myTweets = []

        self.auth = tweepy.OAuthHandler("PxrgqjQnWgGvfATB4hWXlyshv",
                                        "SNKu5GeyPCFIpRpWI7cFIEsKud4N7cstZqTT1qJNcO5PzovkiG")
        self.auth.set_access_token("935832971390738433-PeGkE4PPapZSYjPOdXqeezH5O2lVjvf",
                                   "VwW75cuyO38sCWaJ7nfHbtmF3YHlBoJ4PSzGx903w2qxl")
        self.api = tweepy.API(self.auth)

    def track(self):
        print('Receiving Tweets...')
        time_first_tweet = 0
        halt = True
        last_id = -1

        while halt:
            try:
                new_tweets = self.api.search(q=self.keyword, count=200, lang='en', max_id=str(last_id - 1))
                if not new_tweets:
                    halt = False

                for tweet in new_tweets:

                    if time_first_tweet == 0:
                        time_first_tweet = tweet.created_at

                    elif (time_first_tweet - tweet.created_at).total_seconds() > self.hours * 3600:
                        halt = False

                    else:
                        self.myTweets.append(
                            Tweet(tweet.text, tweet.created_at, tweet.author.screen_name, tweet.author.id,
                                  tweet.author.followers_count))
                    last_id = new_tweets[-1].id
                print(self.myTweets)
            except tweepy.TweepError as e:
                halt = False


