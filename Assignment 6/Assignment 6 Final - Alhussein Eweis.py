import tweepy
import matplotlib.pyplot as plt


class Tweets:
    def __init__(self, tweet_id, tweet_text, tweet_lang):
        self.tweet_id=tweet_id
        self.tweet_text=tweet_text
        self.tweet_lang=tweet_lang


    def __str__(self):
        return "{}-{}-{}".format(self.tweet_id, self.tweet_text, self.tweet_lang)



#login details
consumer_key="K2BGyn2pV4noB91o76MXTYBtN"
consumer_secret="R5I7Vq0UrESGAruloSQmzDP2joqPxIsgoszfpC7O0GLxuihGpE"
access_token="1199412624259244035-KQEqelnvkCaMAIn4NCTfgk7x67C5sZ"
access_token_secret="goER0ldCtcahXyBiYeWfKmtBygH1A0lpiRbcJlBG3bqei"

#Having Twython access my twitter account

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#performing my search on Twitter

my_search=tweepy.Cursor(api.search, q='lebron', result_type='mixed').items(100)



#tweet_details
i=0
count=0
tweet_storing=[]
Labels={}
for tweet in my_search:
    tweet_id=tweet.id
    tweet_text=tweet.text.encode('UTF-8', errors='ignore') #encode the tweets
    tweet_lang=tweet.lang
    if tweet_lang=='en':
        count = count +1
    if not tweet_lang in Labels:
        Labels[tweet_lang]=1
    else:
        Labels[tweet_lang]=Labels[tweet_lang]+1

    
    tweet_storing.append(Tweets(tweet_id,tweet_text,tweet.lang))
    
    
print(Labels)





#Linked List class

class Node(Tweets):
    def __init__(self, cargo=None, next=None):
        self.cargo=cargo
        self.next=next
        
    def __str__(self):
        return str(self.cargo)

node=Node()

#storing tweets in the the linked list
for each in tweet_storing:
    node=each

#node=tweet_storing
    
# matplotlib graphing part
x=Labels.keys()
y=Labels.values()

x_pos=[i for i, _ in enumerate(x)]

plt.title("Tweet Languages Bar Chart")
plt.bar(x_pos,y)  
plt.ylabel("Language occurences")
plt.xlabel("Languages")
plt.xticks(x_pos,x)
plt.show()


#Name: Alhussein Eweis

