#Program:
#   This program is download the batch images.The best way to read the program is open the html and find the tags that i
#write in the program
#History:
#2018-01-26     Vigor       FirstRelease

from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen
import os

html = urlopen("http://www.ivsky.com/tupian/xuejing_t36/index_2.html").read().decode('utf-8')
#find link about images
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("div", {"class": 'pagelist'})

#find link about tags
course_links = soup.find_all('a', {'href': re.compile('/tupian/.*index_.\.html$')})
# print(course_links)
resultURL = ["%s%s" %('http://www.ivsky.com',links['href']) for links in course_links]

for URL in resultURL :
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    img_ul = soup.find_all('div', {'class': "il_img"})
    print(len(img_ul))

    os.makedirs('./img/', exist_ok=True)
    for ul in img_ul:
        imgs = ul.find_all('img')
        for img in imgs:
            url = img['src']
            r = requests.get(url, stream=True)
            image_name = url.split('/')[-1]
            with open('./img/%s' % image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
            print('Saved %s' % image_name)

