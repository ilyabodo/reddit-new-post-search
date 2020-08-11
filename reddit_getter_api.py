import praw
from datetime import datetime
import time

class Item:
	def __init__(self, title='', body='', ids=''):
		self.title = title
		self.body = body
		self.id = ids


sub_reddit = "SUBREDDIT_NAME_HERE"
# All keywords that the program should search posts for
keywords = ["apple", "banana"] # Capitalization doesn't matter here

time_length = 1 #Amount of time you want to run script in hours

# API keys from the reddit API page
client_id = "PUT_CLIENT_ID_HERE"
client_secret = "PUT_CLIENT_SECRET_HERE"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent="my user agent")

items_list = list() # List to hold all the Items
id_list = list() # Keeps track of post ids so new Item objects aren't constantly created

def search():
	for submission in reddit.subreddit(sub_reddit).new(limit=5):
		# More attributes/properties of each post can be gathered here
		entree = Item(submission.title, submission.selftext, submission.id)
		# Adds and prints any posts that havent already been recorded
		if entree.id not in id_list:
			items_list.append(entree)
			id_list.append(entree.id)
			# Searches each post for each of the keywords
			for word in keywords:
				if (word.lower() in entree.title.lower() 
						or word.lower() in entree.body.lower()):
					print_item(word, entree)

# Function that prints all the information to the console
def print_item(keyword: str, item: Item):
	print("--------------------------") # Visual line seperator
	print("Keyword found: ", keyword)
	print(datetime.now().strftime('%Y/%m/%d %I:%M:%S')) # Date formating
	print("Title: " + item.title)
	print("Body: " + item.body.strip())

print("Starting")

for x in range(720*time_length): # Runtime in hours given the 5 second sleep function below
	search()
	time.sleep(5) # Changes the frequency of api calls	

print("Completed")
