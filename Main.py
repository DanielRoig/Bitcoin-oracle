from Crawler import Crawler
import BitcoinData as Btc
from Broker import Broker
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Create, setup and execute the crawler
twitterCrawler = Crawler("Bitcoin", 1, "en")
twitterCrawler.track()

# Create the Broker
broker = Broker()

# Broker analyses the sentiment of all the tweets retrieved
broker.analyse(twitterCrawler.myTweets)

print('broker.tweet_amount:', broker.tweet_amount)
print('broker.score_avg:', broker.score_avg)
print('broker.score_sum:', broker.score_sum)
print('broker.follower_based_score:', broker.follower_based_score)

bitcoin = Btc.BitcoinData()
print(bitcoin.averageData())

