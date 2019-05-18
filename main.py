import tweepy
import datetime


class Tweet:
    def __init__(self, tweet_text, tweet_date, user_nickname, user_id, user_followers):
        self.tweet_text = tweet_text
        self.tweet_date = tweet_date
        self.user_nickname = user_nickname
        self.user_id = user_id
        self.user_followers = user_followers
        self.behaviour = 0
        

auth = tweepy.OAuthHandler("PxrgqjQnWgGvfATB4hWXlyshv", "SNKu5GeyPCFIpRpWI7cFIEsKud4N7cstZqTT1qJNcO5PzovkiG")
auth.set_access_token("935832971390738433-PeGkE4PPapZSYjPOdXqeezH5O2lVjvf", "VwW75cuyO38sCWaJ7nfHbtmF3YHlBoJ4PSzGx903w2qxl")


api = tweepy.API(auth)

myTweets = []

last_id = -1
while True:
    try:
        new_tweets = api.search(q="Bitcoin", count=200, lang='en', max_id=str(last_id - 1))
        if not new_tweets:
            break
        for tweet in new_tweets:
        	myTweets.append(Tweet(tweet.text, tweet.created_at, tweet.author.screen_name, tweet.author.id, tweet.author.followers_count))

        last_id = new_tweets[-1].id

        if len(myTweets) > 30:
        	break;

    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

for tweet in myTweets:
	print tweet.tweet_text
	print tweet.tweet_date
	print tweet.user_nickname
	print tweet.user_id
	print tweet.user_followers

	print "----------------------------"






