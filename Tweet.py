

class Tweet:
    def __init__(self, tweet_text, tweet_date, user_nickname, user_id, user_followers):
        self.tweet_text = tweet_text
        self.tweet_date = tweet_date
        self.user_nickname = user_nickname
        self.user_id = user_id
        self.user_followers = user_followers
        self.behaviour = 0
        self.sentiment = 0
        self.financial_weight = 0
