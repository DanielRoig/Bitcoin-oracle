import twitterCrawler as crawler

twitterCrawler=crawler.Crawler("Bitcoin",1)
twitterCrawler.track()

for tweet in twitterCrawler.myTweets:
	print tweet.tweet_text
	print tweet.tweet_date
	print tweet.user_nickname
	print tweet.user_id
	print tweet.user_followers

	print "----------------------------"


