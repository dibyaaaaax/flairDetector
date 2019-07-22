import praw
import datetime
import preprocessing
import pandas as pd
my_id="tAljm_xaleW1PQ"
my_secret="xri1XtaJJ8EANnDnpbvAIHEKlBg"
my_agent="precog"
reddit = praw.Reddit(client_id= my_id, client_secret= my_secret, user_agent=my_agent)

def findDataOn(query, flair):
    posts = reddit.subreddit('india').search(query, syntax = 'lucene', limit=170)
    all_posts = []
    id_list=[]
    c=0
    for post in posts:
        
        if post.link_flair_text!=None:

            if (post.link_flair_text == flair):
                entry={}
                entry["flair"] = post.link_flair_text
                entry["title"] = post.title
                entry["time"] = datetime.datetime.fromtimestamp(post.created)
                entry["link"] = post.url
                entry["_id"] = post.id
                entry["body"] = post.selftext
                entry["commentNum"] = post.num_comments
                entry["upvotes"] = post.ups
                entry["comments"] = ""

                post.comments.replace_more(limit=0)
                for comment in post.comments.list():
                    if comment.body!="[removed]":
                        entry["comments"]=entry["comments"] + " " + str(comment.body)
                #entry["comments"] = preprocessing.preprocess(entry["comments"])

                entry["titleComments"] = entry["title"] + entry["comments"]
                if (entry["_id"] not in id_list):
                    c+=1
                    print(c)
                    all_posts.append(entry)
                    id_list.append(entry["_id"])

    return all_posts                

######https://praw.readthedocs.io/en/latest/