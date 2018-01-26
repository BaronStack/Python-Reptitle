#Program:
#   This program is scrap a series of html link.You can open the html and inspect the element.
#History:
#2018-01-25     Vigor       FirstRelease


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("http://www.ivsky.com/tupian/xuejing_t36/index_2.html").read().decode('utf-8')
#find link about images
soup = BeautifulSoup(html, features='lxml')

#find the tags  div has the class named 'pagelist',and get all this element
img_links = soup.find_all("div", {"class": 'pagelist'})

#find link about tags with regular expression
course_links = soup.find_all('a', {'href': re.compile('/tupian/.*index_.\.html$')})
# print(course_links)
for link in course_links:
    print(link['href'])