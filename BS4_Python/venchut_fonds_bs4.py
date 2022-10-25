import time
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://connect.visible.vc/investors'     

headers = {"accept": "text/css,*/*;q=0.1", 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

}

req = requests.get(url, headers=headers)

src = req.text 
print(src)



