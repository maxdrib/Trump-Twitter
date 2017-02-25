import twitter

with open('credentials.config', 'r') as f:
    consumer_key = f.readline()
    consumer_secret = f.readline()
    access_token_key = f.readline()
    access_token_secret = f.readline()

api = twitter.Api(consumer_key=consumer_key, 
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)
print "success"

