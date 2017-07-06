import requests 
from bs4 import BeautifulSoup 

url = "http://www.mon-poeme.fr/citations-enseigner-1/"
r = requests.get(url)

soup = BeautifulSoup(r.content)

q_data = soup.find_all("div", {"class": "post"})

for item in q_data:
	print item.text
