from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

from TwitterReader import consumer_key, consumer_secret, access_secret, access_token


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python_blm.json', 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#blm'])
