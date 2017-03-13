import json

def load_key():
    with open('config.json') as json_data:
        api_key = json.load(json_data)
        return api_key

def store_key():
    api_key = {}
    api_key["consumer_key"] = input("Consumer Key: ")
    api_key["consumer_secret"] = input("Consumer Secret: ")
    api_key["access_key"] = input("Access Key: ")
    api_key["access_secret"] = input("Access Secret: ")

    with open("api_key.json", 'w') as f:
        json.dump(api_key, f, ensure_ascii=True,
                           sort_keys=True,
                           indent=4,
                           separators=(',', ': '))
