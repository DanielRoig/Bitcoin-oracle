from Crawler import Crawler
import CryptoData as CryptoData
from Broker import Broker
from pprint import pprint

def retrieve_tweets(currency, hours, language):

    # Fill up a dictionary with the crypto abbreviation ("Bitcoin" : "BTC")
    currency_list = {}
    currency_list_file = open('assets/currency_list.txt', "r")

    for line in currency_list_file:
        line = line.split(' ')
        currency_list[line[0]] = line[1].rstrip()

    currency_abbreviation = currency_list[currency.capitalize()]

    # Create, setup and execute the crawlers
    # We develop 3 different crawlers for incremented accuracy
    # The word format changes in every one, ex: (bitcoin, Bitcoin, BTC)

    currency_capital_crawler = Crawler(currency.capitalize(), hours, language)
    currency_lower_crawler = Crawler(currency.lower(), hours, language)
    currency_abbreviation_crawler = Crawler(currency_abbreviation, hours, language)

    # Get all the tweets
    currency_capital_crawler.track()
    currency_lower_crawler.track()
    currency_abbreviation_crawler.track()

    # Create the Brokers
    broker_capital = Broker()
    broker_lower = Broker()
    broker_abbreviation = Broker()

    # Analyze the tweet list
    broker_capital.analyze(currency_capital_crawler.myTweets)             # Bitcoin
    broker_lower.analyze(currency_lower_crawler.myTweets)                 # bitcoin
    broker_abbreviation.analyze(currency_abbreviation_crawler.myTweets)   # BTC

    # Get all the data of the crypto from www.cryptocompare.com
    cryptocurrency = CryptoData.CryptoData()
    cryptodata = cryptocurrency.average_data(currency_abbreviation)

    # Sum of the 3 score result
    tweet_amount = broker_capital.tweet_amount + broker_lower.tweet_amount + broker_abbreviation.tweet_amount
    score_avg = (broker_capital.score_avg + broker_lower.score_avg + broker_abbreviation.score_avg) / 3
    weighted_score = (broker_capital.follower_based_score + broker_lower.follower_based_score + broker_abbreviation.follower_based_score) / 3
    pprint(cryptodata)

    # This index modifies the entire result, it is designed avoid cryptodumbs and fake stuff
    regulator_index = -3

    data = {
        'Cryptocurrency': cryptodata['RAW']['FROMSYMBOL'],
        'Current_price': cryptodata['DISPLAY']['PRICE'],
        'Tweet_amount': tweet_amount,
        'Score_Average': score_avg + regulator_index,
        'Weighted_Score': weighted_score,
        'state': 'OK'
    }

    return data



