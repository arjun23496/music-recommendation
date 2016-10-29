import json
import sys
import re

import pandas as pd

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2718609962-z1P4vsKCHEJ8b0F6qZb2eHHCvAi8qN0c0E9lhqj"
access_token_secret = "XiHiyPHTOq4plYV7WCx844BbbIPprt8kWWRboRElvEfrY"
consumer_key = "ZDRMgVvy7ClZA0Jiu9vaMdlQo"
consumer_secret = "hx0wqFNtMHgedhaoOZOVr9N33tHj1Nce3KHqJZXZzt2EZ57qQR"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self):
        self.ctr = 24029
        self.data_dir = "tweet\ crawler/"

    def on_data(self, data):
        data = json.loads(data)
        # print data
        self.ctr = self.ctr+1

        sys.stdout.write(" %d tweets \r" % (self.ctr))
        sys.stdout.flush()

        data['user']['name'] = re.sub(',','.',data['user']['name'])
        data['text'] = re.sub(',','.',data['text'])

        file_string = str(data['user']['id'])+","+data['user']['name']+","+data['text']+"\n"
        with open(self.data_dir+"tweets_crawler_dataset.csv", "a") as myfile:
            myfile.write(file_string.encode("utf-8"))
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['song', 'music'])
    stream.filter(locations=[-74,40,-73,41])
    # stream.filter(follow=users)