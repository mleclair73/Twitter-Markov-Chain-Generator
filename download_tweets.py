import tweepy
import config
import json
import nltk
import unicodedata
import pprint

nltk.download
api_key = config.load_key()

def print_tweets(list_of_tweetDicts):
    print(json.dumps(l, sort_keys=True,indent=4, separators=(',', ': ')))

def load_json(screen_name):
    with open(screen_name + '.json', 'r') as f:
        return json.load(f)

def save_json(file_name, data):
    with open((file_name + '.json'), 'w') as f:
        json.dump(data, f, ensure_ascii=True,
                           sort_keys=True,
                           indent=4,
                           separators=(',', ': '))

def get_tweets(screen_name, get_all = False):

    #setup api key
    auth = tweepy.OAuthHandler(api_key['consumer_key'], api_key['consumer_secret'])
    auth.set_access_token(api_key['access_key'], api_key['access_secret'])

    api = tweepy.API(auth)

    #get first 200 tweets
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #dictionary to hold tweets
    all_tweets = []
    all_tweets.extend(new_tweets)

    #save id of last tweet - 1
    oldest = all_tweets[-1].id - 1


    #get all remaining tweets
    if get_all:
        while (len(new_tweets) > 0):
            #get all tweets older than max_id
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

            all_tweets.extend(new_tweets)

            oldest = all_tweets[-1].id -1

    #all tweets available are collected
    #convert to list of dict's
    #print(vars(all_tweets[1]))

    list_of_tweetDicts = [{"tweetID"        :tweet.id,
                           "userID"         :tweet.user.id,
                           "screen_name"    :tweet.user.screen_name,
                           "time"           :str(tweet.created_at),
                           "coordinates"    :tweet.coordinates,
                           "rt_count"       :tweet.retweet_count,
                           "source"         :tweet.source,
                           "text"           :unicodedata.normalize('NFKD', tweet.text)
                           #'text'           :tweet.text.replace('\\xe2\\x80\\x99','\'').replace('\u2024', '.').replace('\u200b', '')#.encode('utf-8', errors='ignore')
                           } for tweet in all_tweets]

    save_json(screen_name,list_of_tweetDicts)
