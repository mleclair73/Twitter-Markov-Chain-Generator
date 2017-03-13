import download_tweets
import nltk
#nltk.download()
from nltk.corpus import stopwords


def words_to_prob(words):
    probs = {}
    for w in words:
        if w not in probs:
            probs[word] = 1
        else:
            probs[word] += 1
    probs ={k:(v/len(words)) for k, v in probs.items()}
    print(probs)

def filter_bag(words, stopwords=True, urls=True, mentions=True):
    #remove stopwords
    if stopwords:
        words = [w for w in words if not w in stopwords.words("english")]
    #remove urls
    if urls:
        words = [w for w in words if "http" not in w and "www" not in w]
    #remove @users
    if mentions:
        words = [w for w in words if not "@" in w]
    return words

def bag_of_words(list_of_tweetDicts):
    word_list = []
    #print(list_of_tweetDicts)
    words = [w for tweet in list_of_tweetDicts for w in tweet["text"].split(" ")  ]

    print(words)
    return words

words_to_prob(bag_of_words(download_tweets.load_json("TechCrunch")))
