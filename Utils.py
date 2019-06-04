from Crawler import Crawler
import CryptoData as CryptoData
from Broker import Broker


def retrieve_tweets(currency, hours, language):

    # Create, setup and execute the crawler
    twitter_crawler = Crawler("bitcoin", 1, "en")
    twitter_crawler.track()

    # Create the Broker
    broker = Broker()

    # Broker analyses the sentiment of all the tweets retrieved
    broker.analyse(twitter_crawler.myTweets)

    print('broker.tweet_amount:', broker.tweet_amount)
    print('broker.score_avg:', broker.score_avg)
    print('broker.score_sum:', broker.score_sum)
    print('broker.follower_based_score:', broker.follower_based_score)
    print('broker.follower_amount:', broker.follower_amount)

    cryptocurrency = CryptoData.CryptoData()
    print(cryptocurrency.average_data('Ethereum'))
    data = cryptocurrency.average_data(currency)

    if data['state'] == 'OK':

        output_list = {
            'Cryptocurrency': cryptocurrency['FROMSYMBOL'],
            'Current price': cryptocurrency['DISPLAY'] + '$',
            'Tweet amount': broker.tweet_amount,
            'Score Average': broker.score_avg,
            'state': 'OK'
        }

        return output_list

    else:

        data = {
            'state': 'WRONG'
        }
        return data


