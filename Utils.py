from Crawler import Crawler
import CryptoData as CryptoData
from Broker import Broker


def retrieve_tweets(currency, hours, language):


    # Fill up a dictionary with the crypto abbreviation ("Bitcoin" : "BTC")
    currency_list = {}
    currency_list_file = open('assets/currency_list.txt', "r")

    for line in currency_list_file:
        line = line.split(' ')
        currency_list[line[0]] = line[1].rstrip()

    # If currency input is not in the dictionary RIP
    if currency.capitalize() not in currency_list:
        data = {
            'state': 'WRONG_CURRENCY'
        }
        return data

    currency_abbreviation = currency_list[currency.capitalize()]

    # Create, setup and execute the crawlers
    # We develop 3 different crawlers for incremented accuracy
    # The word format changes in every one, ex: (bitcoin, Bitcoin, BTC)

    currency_capital_crawler = Crawler(currency.capitalize(), hours, language)
    currency_lower_crawler = Crawler(currency.lower(), hours, language)
    currency_abbreviation_crawler = Crawler(currency_abbreviation, hours, language)

    currency_capital_crawler.track()
    currency_lower_crawler.track()
    currency_abbreviation_crawler.track()

    # Create the Brokers
    broker_capital = Broker()
    broker_lower = Broker()
    broker_abbreviation = Broker()

    # Broker analyses the sentiment of all the tweets retrieved
    broker_capital.analyse(currency_capital_crawler.myTweets)
    broker_lower.analyse(currency_lower_crawler.myTweets)
    broker_abbreviation.analyse(currency_abbreviation_crawler.myTweets)

    # Get all the data of the crypto from www.cryptocompare.com
    cryptocurrency = CryptoData.CryptoData()
    cryptodata = cryptocurrency.average_data(currency_abbreviation)

    # Sum of the 3 score result
    tweet_amount = broker_capital.tweet_amount + broker_lower.tweet_amount + broker_abbreviation.tweet_amount
    score_avg = (broker_capital.score_avg + broker_lower.score_avg + broker_abbreviation.score_avg) / 3

    data = {
        'Cryptocurrency': cryptodata['FROMSYMBOL'],
        'Current price': cryptodata['DISPLAY'] + '$',
        'Tweet amount': tweet_amount,
        'Score Average': score_avg,
        'state': 'OK'
    }

    return data



