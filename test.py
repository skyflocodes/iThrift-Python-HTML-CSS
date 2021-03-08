# Import libraries -------------------#
#you need to properly import requests and BeautifulSoup on to your computer
from bs4 import BeautifulSoup
import requests
import csv

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
