def most_tweeted(tweets):
    mas_retweeteados = sorted(tweets, key=lambda d: d['retweetCount'])
    mas_retweeteados = mas_retweeteados[-10:]
    return mas_retweeteados

def top_users(tweets):
    tweeteros = dict()
    for tweet in tweets:
        if tweet['user']['id'] not in tweeteros.keys():
            tweeteros[tweet['user']['id']] = 0
        else: 
            tweeteros[tweet['user']['id']] += 1
    tweeteros = sorted(tweeteros.items(), key=lambda x: x[1], reverse=True)
    tweeteros = tweeteros[0:10]

    users = []

    for user in tweeteros:
        for tweet in tweets:
            if tweet['user']['id'] == user[0]:
                users.append(tweet['user'])
                break

    return users
    

def top_days(tweets):
    pass

def top_hashtags(tweets):
    pass

