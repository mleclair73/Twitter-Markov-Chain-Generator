import download_tweets
import nltk
import pprint
import json


chain = {}

def preprocess(words):
    words = [w for w in words if "http" not in w and "www" not in w]
    words = [w.replace('\\s+', '') for w in words]
    words = [w.replace('"', '') for w in words]
    words = [w.replace('\'', '') for w in words]

    return words

def process_pair(key, val):
    if key in chain:
        if val in chain[key]:
            chain[key][val] += 1
        else:
            chain[key][val] = 1
    else:
        chain[key] = {val:1}

def generate_chain_depth_three(filename):
    tweets = download_tweets.load_json(filename)
    #chain['(NAME)'] = filename
    for tweet in tweets:
        words = tweet["text"].split(' ')
        words = preprocess(words)
        words.insert(0, '*start')
        words.append('*end*')
        for i, word in enumerate(words):
            if word == '':
                continue

            if i + 1 <= len(words) -1:
                word_1 = words[i+1]
                process_pair(word, word_1)

            # if i + 2 <= len(words) -1:
            #     word_2 = words[i+2]
            #     process_pair(' '.join((word, word_1)), word_2)
            #
            # if i + 3 <= len(words) -1:
            #     word_3 = words[i+3]
            #     process_pair(' '.join((word, word_1, word_2)), word_3)

    '''
    Take each tweet
    Break each tweet into list of words
    take word at index i
    word at index j
    if chain contains list[i]
        true:
        if subchain contains list[j]
            subchain[list[j]] ++
        else
            subchain[list[j]] = 1
    else
        chain[list[i]] = {list[j]:1}

    '''
    #pprint.pprint(chain)
    return chain

def normalize_data(chain):
    normalized = {}

    for key, val in chain.items():
        #pprint.pprint(key)
        #pprint.pprint(val)
        total = sum(val.values())

        val_norm = {}
        for sub_key, sub_val in val.items():
           val_norm[sub_key] = float(sub_val)/total

        normalized[key] = val_norm


    #pprint.pprint(normalized)
    with open('TechCrunch_mkv_d1.json', 'w') as f:
        #pprint.pprint(normalized, f)
        json.dump(normalized, f, indent = 1,
                                separators=(',', ': '))    #return normalized

def pick_next(next_states, f):
    d = 0
normalize_data(generate_chain_depth_three('TechCrunch'))

''' Structure for JSON
[{...
  'text':...
  ...},
 {},
 {},
 {},]
 '''
