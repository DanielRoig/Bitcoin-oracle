from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Broker:

    def __init__(self):
        self.working = False
        self.tweet_amount = 0
        self.score_sum = 0
        self.score_avg = 0
        self.follower_based_score = 0
        self.follower_amount = 0

    def analyze(self, tweet_list):

        # Initialize Broker
        print(",,,,..............,......... ...   ..............")
        print("..,,...,,...,,,,..,**********,...   .............")
        print("...............///***,,,,,,,***/*,...............")
        print(".....,.... .,((/**,,,,.......,,***/* ............")
        print(".......... /((/***,....   .....,***//. ..........")
        print("..........*##(/**,,...    ......,,**/(...........")
        print(".........*(###(/**,....   ......,,*/((*.......,..")
        print(",,..,,,,.*/#%##(/*,,...........,,,*/((*.,,,,,,*,,")
        print(".........*/%%#(/*,,,....,,.,,,,*//*/((,.........,")
        print(",,,,..,..,(##%((#%((&%*.,,*%&&&/..*/(/*,,,....,.,")
        print(",,....,#(/((#%@@@@@@@@%/,,(@@@@@@@/*/*%*...,,..")
        print(".......*(##/*#@@@@@@@@/,...@@@@@@@@&,,//*,...,,. ")
        print(".......*,##//(&@@@@@%/,....,(@@@@@#*,,//.,,.,,,..")
        print(",,.....,,*#(/**/**..*/,  .,,, .,,,.,,*//,*,,,,*,.")
        print("...... ./#%%(/*,,,,,%((#%(/.....,,,*#(*,,..,,. ")
        print(".........#%&%(/**,,,**,,,..,....,,,,*/#(,,,,***..")
        print("........  (&%%#/*********/*,,,,,,,**/(%*,,,,,*,,.")
        print(",,......  *&%%%((/(%%(,,,,,#&(**///((##,,,,,,,,..")
        print(",......  (&%&%%%#(((((((((//***//((##%#,..,,,,,. ")
        print(".......*&&@&&&&&%%##(/*///*////((##%&@@@%,.,,**..")
        print("......%#(%@@@@&&%%##/*,,,.,*//(###&@@@@%(#(..,.. ")
        print(".....#(**(@@@@@&&%%#(//*/**//((%&&@@@@@&&%%/.....")
        print("**####/*/%@@@@@@@@@&%%%#%%&%%&@@@@@@@@@&&%#.,..")
        print("&&((((*,*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&(#%&%")
        print("&%#(#/,**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&%%%%%")
        print("%(#//////@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@&@&&&%%&&&")
        print("%#/**,//(@@@@@@@@@@@%(***%&&&%%&@&&@@@&@@%&&&&&")

        # Change the state to "working" and initialize variables
        self.working = True
        self.tweet_amount = len(tweet_list)

        if self.tweet_amount != 0:
            analyzer = SentimentIntensityAnalyzer()

            # Loop the tweet list and get all the results of sentiment analysis, updating the tweet object
            for tweet in tweet_list:

                # Get the sentiment of the tweet
                result = analyzer.polarity_scores(tweet.tweet_text)

                # Set up the score into the tweet object
                tweet.sentiment = result['compound']

                # Add the financial dictionary weight
                self.financial_dictionary_analysis(tweet)

                # Sum scores
                self.score_sum += tweet.sentiment

                # Compute the score-followers algorithm
                self.follower_based_score += self.analyse_followers_score(tweet)

                # Get follower count
                self.follower_amount += tweet.user_followers

            # Compute the standard avg
            self.score_avg = self.score_sum / self.tweet_amount

            # Change the state to "not working"
            self.working = False

        else:
            return False

    @staticmethod
    def financial_dictionary_analysis(tweet):
        financial_dictionary = open('assets/financial_dictionary.txt', 'r')

        # Loop the financial dictionary ('Word', 'score'), score is 1 (positive) or 0 (negative)
        for line in financial_dictionary:

            word_caps = line.split(',')[0]
            word_lower = line.split(',')[0].lower()
            word_score = line.split(',')[1]

            # If tweet has a financial word
            if word_lower in tweet.tweet_text or word_caps in tweet.tweet_text:

                # If word is negative
                if word_score == '0':
                    tweet.sentiment = -0.8
                    tweet.financial_weight = -1

                # If word is positive
                else:
                    tweet.sentiment = 0.8
                    tweet.financial_weight = 1

    @staticmethod
    def analyse_followers_score(tweet):

        # 0 - 20.000 followers
        if tweet.user_followers <= 20000:
            score = 0.05 * tweet.sentiment

        # 20.000 - 100.000 followers
        elif 20000 < tweet.user_followers <= 100000:
            score = 0.12 * tweet.sentiment

        # 100.000 - 500.000 followers
        elif 100000 < tweet.user_followers <= 500000:
            score = 0.24 * tweet.sentiment

        # 500.000 - 1M followers
        elif 500000 < tweet.user_followers <= 1000000:
            score = 0.6 * tweet.sentiment

        # 1M - 5M followers
        elif 1000000 < tweet.user_followers <= 5000000:
            score = 1.2 * tweet.sentiment

        # + 5M followers
        elif tweet.user_followers > 5000000:
            score = 2.5 * tweet.sentiment

        else:
            score = 0

        return score


