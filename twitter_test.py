#import twitter
from twython import Twython

with open('credentials.config', 'r') as f:
    all_credentials = f.readlines()

twitter = Twython(all_credentials[0][:-1], all_credentials[1][:-1], all_credentials[2][:-1], all_credentials[3][:-1])
twitter.verify_credentials()
print "successfully verified credentials"



