from bs4 import BeautifulSoup
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"

web_page = urllib.request.urlopen(url)
soup = BeautifulSoup(web_page, 'html.parser')

# get all the ITM people names from the anchor tags
h2_elements = soup.find_all('h2', class_='title')
itm_people = []
for h2 in h2_elements:
    span = h2.find('span')
    if span:
        itm_people.append(span.text)

print(f"There are {len(itm_people)} ITM People:")
print(itm_people)
