def most_tweeted(tweets):
    mas_retweeteados = sorted(tweets, key=lambda d: d['retweetCount'])
    mas_retweeteados = mas_retweeteados[-10:]
    return mas_retweeteados

def top_users(tweets):
    pass

def top_days(tweets):
    pass

def top_hashtags(tweets):
    pass

