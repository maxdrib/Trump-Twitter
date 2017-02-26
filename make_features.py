import sys
import numpy as np

keywords_directory = "keywords/"

class Make_Features(object):
    def __init__(self):
        keyword_files = ['fake_news.txt', 'finance.txt', 'negative.txt', 
                            'family.txt', 'government.txt', 'positive.txt']
        self.keywords = []
        file_number = 0
        self.numKeywords = 0
        for filename in keyword_files:
            with open(keywords_directory+filename, 'r') as f:
                all_text = f.readlines()    
            self.keywords.append(all_text)
            print self.keywords[file_number]
            self.numKeywords += len(list(self.keywords[file_number]))
            file_number += 1

    def read_tweets(self, filepath):
        with open(filepath, 'r') as f:
            self.tweets = f.readlines()
        #print self.tweets

    def generate_features(self):
        self.data = []
        tweet_idx = 0
        for tweet in self.tweets:
            instance_vect = np.zeros(self.numKeywords+1)
            feature_index = 0
            for filename in self.keywords:
                for word in filename:
                    if word[:-1] in tweet:
                        instance_vect[feature_index] = 1
                    feature_index +=1
            self.data.append(instance_vect)
            tweet_idx += 1

if __name__=="__main__":
    make_features = Make_Features()
    print sys.argv[1]
    make_features.read_tweets(sys.argv[1])
    make_features.generate_features()
