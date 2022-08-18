from datetime import date


def most_tweeted(tweets):
    mas_retweeteados = sorted(tweets, key=lambda d: d['retweetCount'])
    mas_retweeteados = mas_retweeteados[-10:]
    return mas_retweeteados

def top_users(tweets):
    tweeteros = dict()
    for tweet in tweets:
        if tweet['user']['id'] not in tweeteros.keys():
            tweeteros[tweet['user']['id']] = 1
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
    dias = dict()
    for tweet in tweets:
        if str(tweet['date'][0:10]) not in dias.keys():
            dias[str(tweet['date'][0:10])] = 1
        else:
            dias[str(tweet['date'][0:10])] += 1

    dias = sorted(dias.items(), key=lambda x: x[1], reverse=True)
    dias = dias[0:10]

    return dias

 

def top_hashtags(tweets):
    pass

