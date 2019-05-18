import twitterCrawler as crawler
import bitcoinData as btc

twitterCrawler=crawler.Crawler("Bitcoin",1,"en")
twitterCrawler.track()

for tweet in twitterCrawler.myTweets:
	print tweet.tweet_text
	print tweet.tweet_date
	print tweet.user_nickname
	print tweet.user_id
	print tweet.user_followers

	print "----------------------------"



bitcoin=btc.BitcoinData()
print bitcoin.averageData()
