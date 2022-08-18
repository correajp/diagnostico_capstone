import json 
from functions import most_tweeted

if __name__ == '__main__':
    tweets = []
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweets.append(json.loads(line))

    print(most_tweeted(tweets))

  