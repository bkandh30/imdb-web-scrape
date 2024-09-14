import requests
import pandas as pd
from bs4 import BeautifulSoup


#/opt/homebrew/bin/chromedriver

url = "https://www.imdb.com/chart/top/"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')
data = []

for movie in movies:
    title = movie.find('h3', class_='ipc-title__text').text.strip()
    year = movie.find('span', class_='cli-title-metadata-item').text.strip()
    rating = movie.find('span', class_='ipc-rating-star').text.strip()
    rating = rating.split()[0]
    watched = ""
    data.append([title, year, rating, watched])

print(data)
print(len(data))
df = pd.DataFrame(data, columns=['Title', 'Year', 'Rating', "Watched"])
df.to_excel('imdb_top250.xlsx')