#import twitter
from twython import Twython
import json

with open('credentials.config', 'r') as f:
    all_credentials = f.readlines()

twitter = Twython(all_credentials[0][:-1], all_credentials[1][:-1], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(all_credentials[0][:-1], access_token=ACCESS_TOKEN)
#twitter.verify_credentials()
print "successfully verified credentials"

tweets = twitter.get_user_timeline(screen_name='realDonaldTrump')

with open('recent_tweets', 'w+') as o:
    recent_tweets = o.readlines()
for tweet in tweets:
    if tweet['text'] in recent_tweets:
        continue
    else:
        print "do things"

with open('recent_tweets', 'w') as f:
    for tweet in tweets:
        f.write(tweet['text']+'\n')

