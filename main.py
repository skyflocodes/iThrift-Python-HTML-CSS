# Import libraries -------------------#
#you need to properly import requests and BeautifulSoup on to your computer
# from bs4 import BeautifulSoup
# import requests
# import csv
# from django.http import HttpResponse
#
# with open('index.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#
# source1 = requests.get('https://ebay.ca/').text
#
# soup = BeautifulSoup(source1, 'lxml')
#
# csv_file = open('cms _scrape', 'w')
#
# csv_writer = cvs.writer(csv_file)
# csv_writer.writerow(['brandname', 'price', 'image'])
# csv_write
#
# for article in soup.find_all('article')
#     brandname = article.div.text
#     print headline
#
# match = soup.titletext
# print(match)
# soup = BeautifulSoup(page.content, 'html.parser')
#
# # we need to figure out how to link the search bar to the search value
# search =
#
# # link the search value into each url in the correct position
#
# ebay = requests.get(ebay_url)
# kijiji = requests.get(kijiji_url)
# grailed = requests.get(grailed_url)
# #testing the url
#
# for span in soup.find_all(class_='amt'):
#     print(span.get_text())


# Import libraries -------------------#
#you need to properly import requests and BeautifulSoup on to your computer
from flask import request,redirect
from bs4 import BeautifulSoup
import requests
import csv
import cgi

form=cgi.FieldStorage()
input_text = form.getfirst("textinput")

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print "<p>%s</p>"%input_text
print "</body>"
print "</html>"

@app.route('/test',methods = ['POST'])
def test():
    print("test")

page = requests.get("https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xsocks.TRS0&_nkw=socks&_sacat=0")

soup = BeautifulSoup(page.content, 'html.parser')

with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)


# ebay
#prints out all of the prices
# for span in soup.find_all(class_='amt'):
#     print(span.get_text())


# prints out all of the titles
# for title in soup.find_all(class_='vip'):
#     print(title.get_text())

# #prints out the image url
for image in soup.find_all(class_='img'):
    print(image.get_text())
    # print(image.span)
    # print(image.vip)
    print(image.img)
    writer.writerow(image.get_text(), image.img)


# links = soup.find('figure').find_all('img', src=True)
# for link in links:
#     timestamp = time.asctime()
#     txt = open('%s.jpg' % timestamp, "wb")
#     link = link["src"].split("src=")[-1]
#     download_img = urllib2.urlopen(link)
#     print(txt)
    # txt.write(download_img.read())
    #
    # txt.close()
