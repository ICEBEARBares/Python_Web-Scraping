print("FOR EDUCATIONAL USING PURPOSE ONLY")
print("Starting Scraping Target Website...")

#DON'T FORGET TO INSTALL "pip install beautifulsoup4"
#DON'T FORGET TO INSTALL "pip install requests"
from bs4 import BeautifulSoup
import requests as req

resp = req.get('https://www.acep.ac.th/')

web = BeautifulSoup(resp.text, 'lxml')

with open("result.html", "w", encoding='utf-8') as file:
    file.write(str(web))

print("PRINTED RESULT TO result.html")
print(web.title)
print(web.body)

print("Ended Scraping Target Website...")