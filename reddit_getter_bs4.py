import bs4
from urllib.request import urlopen
import time
from random import randint
from datetime import datetime

# List of all keywords that user wants to search for
keywords = ["python", "tutorial"]  # Capitalization doesn't matter here

url = 'https://www.reddit.com/r/python/new/'  # Subreddit url with /new

time_length = 1  # Amount of time the script will run for (in hours)

already_found = list()
def search():
	# This often errors out with bad gateway errors, try except block
	# catches it and basically ignores it
	try:
		source = urlopen(url).read().decode('utf-8')
		soup = bs4.BeautifulSoup(source, "lxml")
		titles = list()  # Initalizing the title/body lists for this scape
		bodies = list()
		
		for x in soup.findAll("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}):
			titles.append(x.text)
		for y in soup.findAll("p", {"class": "_1qeIAgB0cPwnLhDF9XSiJM"}):
			bodies.append(y.text)

		for title in titles:
			if not title in already_found:
				for key in keywords:
					if key in title.lower():
						print("--------------")  # Visual spacing
						print("Keyword found: ", key)
						print(datetime.now().strftime('%Y/%m/%d %I:%M:%S'), title)
						already_found.append(title)
		
		for body in bodies:
			if not body in already_found:
				for key in keywords:
					if key in body.lower():
						print("--------------")  # Visual spacing
						print("Keyword found: ", key)
						print(datetime.now().strftime('%Y/%m/%d %I:%M:%S'), body)
						already_found.append(body)

	except:
		return			

print("Starting")

for x in range(720*time_length):
	search()
	time.sleep(randint(3,7))  # Slight randomness in interval helps reduce bad gateway errors

print("Completed")	