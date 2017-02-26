with open('keywords/parsed_companies.txt', 'r') as f:
    companies = f.readlines()

with open('recent_tweets', 'r') as f:
    tweets = f.readlines()
for company in companies:
    #print company
    for word in company.split():
        print word
        for tweet in tweets:
            if word in tweet:
                print tweet, word.upper()
