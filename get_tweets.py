#import twitter
from twython import Twython
import json

# Read in credentials
with open('credentials.config', 'r') as f:
    all_credentials = f.readlines()

# Generate initial twitter object to get Access Token
twitter = Twython(all_credentials[0][:-1], all_credentials[1][:-1], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

# Generate twitter object to make API calls
twitter = Twython(all_credentials[0][:-1], access_token=ACCESS_TOKEN)
print "successfully verified credentials"

# Check for id of last tweet read
with open('last_check_info.txt', 'r') as o:
    since_id = o.readline() 

# Make the API call
tweets = twitter.get_user_timeline(screen_name='realDonaldTrump', count=200, since_id=since_id)

# If nothing new, exit program
if len(tweets)==0:
    print "nothing new"
    exit()

# Otherwise, save id of most recent tweet
with open('last_check_info.txt', 'w') as o:
    o.write(tweets[0]['id_str'])
    
# Iterate over tweets
for tweet in tweets:
    tweet = tweet.lower().translate(' ', ",;:'-\"+").replace("..."," ")
    print "do things"

# Write new recent tweets to file
with open('recent_tweets', 'w+') as f:
    for tweet in tweets:
        tweet = tweet.lower().translate(' ', ",;:'\"-+").replace("..."," ")
        to_post = tweet['text'].encode('utf-8').lower()+'\n'
        f.write(to_post)

