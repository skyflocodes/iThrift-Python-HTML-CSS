# Import libraries -------------------#
#you need to properly import requests and BeautifulSoup on to your computer
import requests
from bs4 import BeautifulSoup
#-------------------------------------#

#not sure what page.content is
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# we need to figure out how to link the search bar to the search value
search =

# link the search value into each url in the correct position
ebay_url = "https://www.ebay.ca/"
kijiji_url = "https://www.kijiji.ca/"
grailed_url = "https://www.grailed.com/"

ebay = requests.get(ebay_url)
kijiji = requests.get(kijiji_url)
grailed = requests.get(grailed_url)

#testing the url
print(ebay_url)
