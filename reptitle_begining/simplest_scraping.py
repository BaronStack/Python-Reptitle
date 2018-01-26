#Program :
# This is a simple test about scrap some tags' from the html

from urllib.request import urlopen
import  re
# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
# print("\nPage title is: ", res[1])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])

res = re.findall(r"<a href=(.*?)>(.*?)</a>",html, flags=re.DOTALL)
print("\nHeadline2 is: ",res[1])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)