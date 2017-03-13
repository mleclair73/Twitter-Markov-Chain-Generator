import tweepy
import config
import pprint
api_key = config.load_key()

def get_all_tweets(screen_name):

    #setup api key
    auth = tweepy.OAuthHandler(api_key['consumer_key'], api_key['consumer_secret'])
    auth.set_access_token(api_key['access_key'], api_key['access_secret'])

    api = tweepy.API(auth)

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #dictionary to hold tweets
    all_tweets = []
    all_tweets.extend(new_tweets)

    #save id of last tweet - 1
    oldest = all_tweets[-1].id - 1

    # while (len(new_tweets) > 0):
    #     #get all tweets older than max_id
    #     new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    #
    #     all_tweets.extend(new_tweets)
    #
    #     oldest = all_tweets[-1].id -1

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
                           "text"           :tweet.text.replace('\\xe2\\x80\\x99',''').encode('utf-8', errors='ignore')
                           } for tweet in all_tweets]
    # [list_of_tweetDicts.append({'ID':tweet.id,
    #                                  'name':tweet.user.id,
    #                                  'text':tweet.text.encode('utf-8', error='ignore'),
    #                                  'time':tweet.created_at,
    #                                  'geo':tweet.geo,
    #                                  'coordinates':tweet.coordinates,
    #                                  'place':tweet.place,
    #                                  'rt_count':tweet.retweet_count,
    #                                  'source':tweet.source,})
    #                       for tweet in all_tweets]

    pprint.pprint(list_of_tweetDicts)
get_all_tweets('TechCrunch')
